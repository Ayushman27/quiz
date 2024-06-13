const { spawnSync } = require('child_process');
const bodyParser = require('body-parser');
const express = require('express');
const path = require("path");

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

// Serve the static html through express. open http://localhost:3000/ to chat
app.use(express.static(path.join(__dirname, "client")));

app.post('/get-response', (req, res) => {
    try {
        const userInput = 'Give a question with 4 options with correct answer';
        const result = spawnSync('python', ["ai.py", userInput], { encoding: 'utf-8' });

        if (result.error) {
            console.error('Error executing Python script:', result.error);
            throw result.error;
        }

        const response = result.stdout;
        console.log("Response from Python script:", response);

        // Check if the response is empty or invalid
        if (!response) {
            throw new Error('No response from Python script');
        }

        res.json({ response });
    } catch (error) {
        console.error('Error in /get-response:', error);
        res.status(500).json({ error: 'Failed to get response from Python script' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
