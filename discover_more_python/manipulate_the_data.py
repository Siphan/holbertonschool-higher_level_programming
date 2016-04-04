import requests
import json
# function to parse json and print specific field
request_headers = {
    'User-Agent': 'Holberton_School',
 'Authorization': '170f8634262556331b3cb1809ffd4eb6e6fd40e1'
}

r = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', request_headers)
c = r.content
j = json.loads(c)

for k in j['items']:
    print k['full_name']
