const https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
        'User-Agent': 'Holberton_School',
        'Authorization': 'token 170f8634262556331b3cb1809ffd4eb6e6fd40e1'
    }
}

var req = https.request(options, function(res) {
    streamToString(res, function(jsonString) {
        console.log(typeof jsonString);
        console.log(jsonString);
    });
});
req.end();

function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
        chunks.push(chunk);
    });
    stream.on('end', () => {
        cb(chunks.join(''));
    });
}
