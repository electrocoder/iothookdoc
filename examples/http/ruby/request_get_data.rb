require 'uri'
require 'net/http'

url = URI("https://iothook.com/api/device/?api_key=76d2628fd60903d3c1f7f8a0&results=1")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Get.new(url)
request["User-Agent"] = 'PostmanRuntime/7.15.2'
request["Accept"] = '*/*'
request["Cache-Control"] = 'no-cache'
request["Postman-Token"] = 'ce2f06c2-817e-414a-8c7a-2c2fc59ad043,8fe93ff6-b857-4978-838e-2d8efac2e6b6'
request["Host"] = 'iothook.com'
request["Accept-Encoding"] = 'gzip, deflate'
request["Connection"] = 'keep-alive'
request["cache-control"] = 'no-cache'

response = http.request(request)
puts response.read_body
