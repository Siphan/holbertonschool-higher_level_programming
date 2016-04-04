import requests
# Function that gets githubs popular python repos and writes json to file.
request_headers = {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token 170f8634262556331b3cb1809ffd4eb6e6fd40e1'
}

r = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', request_headers)

with open('/tmp/35', 'w') as f:
    f.write(r.content)

print "The file was saved!"
