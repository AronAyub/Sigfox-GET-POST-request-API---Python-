
import requests
import requests
from requests.auth import HTTPBasicAuth
import base64
import time

url = "https://api.sigfox.com/v2/devices/xxxxx/messages"
 # https://api.sigfox.com/v2/devices/{id}/messages

#the token is generated by encoding login:password in Base 64
print("----TOKEN----")
login = 'xxxxxxxxxxxxxxx'
password = 'xxxxxxxxxxxxxxxxxxxxx'
token = login+":"+password
print("Token:", base64.b64encode(token.encode("ascii")).decode("ascii"))
print()
#Once the token is generated, you can use the token directly in your code, it is safer in case your code leaks.
# print("----SOLUTION 1----")
headers = {
  'Authorization': 'Basic xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}
response = requests.get(url, headers=headers)
print(response.text)
print()

time.sleep(2) #just because I do 2 API requests in a row, Sigfox limits to 1 request per second, so I need to slow my strict dow




# decoder try this at free time

# var parser = require('sigfox-parser')
# function convertPayload(data) {
#     var parsed = parser(data, format);
#     var moduleTemp = (parsed.moduleTemp / INT16_t_MAX * 120).toFixed(2);
#     var dhtTemp = (parsed.dhtTemp / INT16_t_MAX * 120).toFixed(2);
#     var dhtHum = (parsed.dhtHum / UINT16_t_MAX * 110).toFixed(2);
#     var heatIndex = computeHeatIndex(dhtTemp, dhtHum, false).toFixed(2);

#     var result = {
#         moduleTemp: moduleTemp,
#         dhtTemp: dhtTemp,
#         dhtHum: dhtHum,
#         heatIndex: heatIndex
#   }
#   return result
# }



