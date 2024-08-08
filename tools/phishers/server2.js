const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
const port = 3000;

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

// Middleware to get client's IP address
app.use((req, res, next) => {
    req.clientIp = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    next();
});

// Endpoint to save GPS location and IP address
app.post('/savelocation', express.json(), (req, res) => {
    const { latitude, longitude } = req.body;
    const ipAddress = req.clientIp;
    const logData = `IP Address: ${ipAddress}, Latitude: ${latitude}, Longitude: ${longitude}\n`;
    fs.appendFile('logs.txt', logData, (err) => {
        if (err) {
            console.error('Error saving location and IP:', err);
            res.status(500).send('Internal Server Error');
        } else {
            res.send('Location and IP saved');
        }
    });
});

// Redirect to permissions.html by default
app.get('*', (req, res) => {
    res.redirect('/permissions.html');
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
