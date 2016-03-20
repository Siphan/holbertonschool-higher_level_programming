require 'HTTPClient' #library

extheaders = { 
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 170f8634262556331b3cb1809ffd4eb6e6fd40e1' #token from Discover JS project
}

clnt = HTTPClient.new #function assigned to a variable
response = clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', query = nil, extheaders) #content fetched is stored in a variable

output = File.open( "/tmp/35", "w" ) #write to file /tmp/35
output << response #writes fetched data in the created file
output.close

puts "The file was saved!" #prints string
