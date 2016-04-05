""" This program parses the response from Github's API when requesting 
    the 30 most popular Python projects to a file into a JSON format and
    prints the name of each project
"""

from urllib2 import Request, urlopen, URLError
import json

request_headers = {
    'User-Agent': 'Holberton School',
    'Authorization': 'token 170f8634262556331b3cb1809ffd4eb6e6fd40e1'
}

request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers=request_headers)

try:
            response = urlopen(request)
            string = response.read()
            parsed = json.loads(string)

            for item in parsed["items"]:
                        print item.get("full_name")
except URLError, e:
        print "Error code: ", e
        
