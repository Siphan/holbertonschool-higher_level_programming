require 'HTTPClient'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 170f8634262556331b3cb1809ffd4eb6e6fd40e1'
}

clnt = HTTPClient.new
response = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', nil, extheaders) #replaced 'query = nil' by 'nil'
json = JSON.parse(response) #parsing JSON string
items = json["items"] #converting JSON string into Ruby hash

full_names = items.map{ |item|  item["full_name"] }.join("\n") #creates hash with key items using Array#map and Array#join methods

# Array#map returns a new array filled with whatever gets returned by the block each time it runs
# Array#join method (the argument to join is what to insert between the strings - in this case a new line):

puts full_names #prints the full names of the most popular Ruby projects on GitHub
