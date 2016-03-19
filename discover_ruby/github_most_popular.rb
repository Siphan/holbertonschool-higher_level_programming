require 'HTTPClient'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token token 170f8634262556331b3cb1809ffd4eb6e6fd40e1'
}

clnt = HTTPClient.new
puts clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', query = nil, extheader = {})

