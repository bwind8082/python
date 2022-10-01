# importing the requests library
import requests
URL = "http://maps.googleapis.com/maps/api/geocode/json"
  
# location given here
location = "gujarart technological university"
PARAMS = {'address':location}
r = requests.get(url = URL, params = PARAMS)
# extracting data in json format
data = r.json()
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      %(latitude, longitude,formatted_address))
