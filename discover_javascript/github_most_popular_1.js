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
    res.on('data', function(d) {
	process.stdout.write(d);
    });
});
req.end();
