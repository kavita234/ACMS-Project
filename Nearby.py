import geocoder
from geopy.geocoders import Nominatim
import requests
import csv
import pprint

with open('Nearby.csv', mode='w', newline='') as output:
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Business Name","Address","Municipality","Business Category","Country"])
with open('clusters.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        lat=(row[1])
        lon=(row[0])
        result = requests.get("https://api.tomtom.com/search/2/nearbySearch/.json?lat="+lat+"&lon="+lon+"&countrySet=IN&idxSet=POI&radius=2000&categorySet=9361,9361067,"
        +"9361051,7320002,9361063,7315149,7326,7373,7327,9913&key=vDjUYMm75UyPwfH0vRJG9meyxAXgRhjT")
       # pprint.pprint(result.street_address)
        data = result.json()
        #pprint.pprint(data['results']['address'])
        with open('Nearby.csv', mode='a', newline='') as output:
                    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    for x in data['results']:
                         writer.writerow([x['poi']['name'],x['address']['freeformAddress'],x['address']['municipalitySubdivision'],x['poi']['categories'],x['address']['country']])
       # pprint.pprint(result.state)
       #p pprint.pprint(result.country)

