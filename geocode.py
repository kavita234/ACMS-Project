import geocoder
from geopy.geocoders import Nominatim
import requests
import csv
import pprint

with open('Address.csv', mode='w', newline='') as output:
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Address","Municipality","Country"])
with open('clusters.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        lat=(row[0])
        lon=(row[1])
        result = requests.get("https://api.tomtom.com/search/2/reverseGeocode/crossStreet/"+lat+","+lon+".json?key=vDjUYMm75UyPwfH0vRJG9meyxAXgRhjT")
       # pprint.pprint(result.street_address)
        data = result.json()
        #pprint.pprint(data['results']['address'])
        with open('Address.csv', mode='a', newline='') as output:
                    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    for x in data['addresses']:
                         writer.writerow([x['address']['freeformAddress'],x['address']['municipalitySubdivision'],x['address']['country']])
                         pprint(x['address']['freeformAddress'] )
        

