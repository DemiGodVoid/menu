const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
const port = 3000;

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

// Endpoint to save GPS location
app.post('/savelocation', express.json(), (req, res) => {
    const { latitude, longitude } = req.body;
    const logData = `Latitude: ${latitude}, Longitude: ${longitude}\n`;
    fs.appendFile('logs.txt', logData, (err) => {
        if (err) {
            console.error('Error saving location:', err);
            res.status(500).send('Internal Server Error');
        } else {
            res.send('Location saved');
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
