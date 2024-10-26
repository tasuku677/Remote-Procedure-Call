const net = require('net');
const fs = require('fs').promises;
const { Buffer } = require('buffer');

async function sendRequest(request) {
    return new Promise((resolve, reject) => {
        const client_server = net.connect('./tmp/socket_file', () => {
            console.log('Connected to server');
            client_server.write(JSON.stringify(request));
        });

        client_server.on('data', (data) => {
            data = JSON.parse(data);
            console.log('Received data:', data);
            client_server.end();
        });

        client_server.on('end', () => {
            resolve();
            console.log('Disconnected from server');
        });

        client_server.on('error', (err) => {
            console.error('Connection error:', err);
            reject(err);
        });
    });
}

async function main() {
    try {
        const data = await fs.readFile('request.json', 'utf8');
        const requests = JSON.parse(data);

        for (const request of requests) {
            try {
                await sendRequest(request);
            } catch (err) {
                console.error(`Error processing request ${request.id}:`, err);
            }
        }
    } catch (err) {
        console.error('Error reading or parsing request file:', err);
    }
}

main();
