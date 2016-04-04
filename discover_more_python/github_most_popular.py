import requests

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 170f8634262556331b3cb1809ffd4eb6e6fd40e1'
}

r = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', request_headers)

print r.content
