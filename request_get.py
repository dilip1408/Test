# import requests as req
#
# location = "delhi technological university"
# PARAMS = {'address':location}
# r = req.get(url="http://maps.googleapis.com/maps/api/geocode/json",params=PARAMS)
#
# data = r.json()
# print(data)

import requests
# import res
import pandas as pd
import json
# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address': location}

# sending get request and saving the response as response object
r = requests.get(url="http://www.floatrates.com/daily/usd.json")
pd.set_option('display.max_columns', 22)
print(type(r))
data = r.json()
#print(data)
print(type(data))
# data = r.read()
# extracting data in json format
# data = json.loads(r)
# data = r.keys()
df = pd.DataFrame.from_dict(data)
# print((df[['eurd']].head()))

# extracting latitude, longitude and formatted address
# of the first matching location
# print(data)
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']
#
# # printing the output
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#       % (latitude, longitude, formatted_address))