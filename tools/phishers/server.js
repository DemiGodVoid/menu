const express = require('express');
const fs = require('fs');
const path = require('path');
const multer = require('multer');
const app = express();
const port = 3000;

app.use(express.json({ limit: '10mb' }));
app.use(express.static(__dirname));

// Serve upload.html at the root path
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public/upload.html'));
});

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'imgs/');
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + '.png');
    }
});

const upload = multer({ storage: storage });

app.post('/upload', (req, res) => {
    const imgData = req.body.image;
    const base64Data = imgData.replace(/^data:image\/png;base64,/, "");
    const filename = path.join(__dirname, 'imgs', Date.now() + '.png');

    fs.writeFile(filename, base64Data, 'base64', err => {
        if (err) {
            console.error(err);
            return res.status(500).json({ success: false, message: 'Failed to save image' });
        }
        res.json({ success: true, message: 'Image saved successfully' });
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
