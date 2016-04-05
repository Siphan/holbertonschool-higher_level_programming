# Function that gets githubs popular python repos and writes json to file.

from urllib2 import Request, urlopen, URLError

request_headers = {
                'User-Agent': 'Holberton School',
                'Authorization': 'token 170f8634262556331b3cb1809ffd4eb6e6fd40e1'
           }

request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers=request_headers)

filename = '/tmp/35'
file = open(filename, 'w')
file.truncate()

try:
            response = urlopen(request)
            string = response.read()
            file.write(string)
            print "The file was saved!"
except URLError, e:
        print "Error code: ", e

        file.close()







