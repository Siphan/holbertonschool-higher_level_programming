""" This program prints the response from Github's API when requesting 
    the 30 most popular Python projects
"""

from urllib2 import Request, urlopen, URLError

request_headers = {
            'User-Agent': 'Holberton School',
            'Authorization': 'token 170f8634262556331b3cb1809ffd4eb6e6fd40e1'
        }

request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers=request_headers)

try:
        response = urlopen(request)
        string = response.read()
        print string
except URLError, e:
    print "Error code: ", e
