const express = require('express');
const request = require('request');
const bodyParser = require('body-parser');
const path = require('path');
require('dotenv').config();

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// Serve the HTML form
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Handle form submission
app.post('/sendMessage', (req, res) => {
    const phoneNumber = req.body.phoneNumber;
    const options = {
        method: 'POST',
        url: `https://graph.facebook.com/v19.0/362243816976323/messages`,
        headers: {
            Authorization: process.env.SECRET_KEY,
            'Content-Type': 'application/json'
        },
        body: {
            messaging_product: 'whatsapp',
            to: phoneNumber,
            type: 'template',
            template: {
                name: 'hello_world',
                language: {
                    code: 'en_US'
                }
            }
        },
        json: true
    };

    request(options, function (error, response, body) {
        if (error) {
            console.error('Error:', error);
            return res.status(500).json({ message: 'Failed to send message' });
        }
        if (body.error) {
            console.error('API Error:', body.error);
            return res.status(500).json({ message: 'Failed to send message' });
        }
        res.json({ message: 'Message sent successfully' });
    });
});

app.listen(3000, () => {
    console.log("Server is running on port 3000");
});
