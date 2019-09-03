import urllib, json
import csv

import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = "https://www.YOURURL.com" # Your store URL
consumer_key = "YourConsumerKey" # Your consumer key
consumer_secret = "YourConsumerSecret" # Your consumer secret
date_min = "2019-08-01"
date_max = "2019-08-31"

APIurl = url + "/wp-json/wc/v3/reports/top_sellers?date_min=" + date_min + "&date_max=" + date_max + "&consumer_key=" + consumer_key + "&consumer_secret=" + consumer_secret

response = urllib.urlopen(APIurl)
data = json.loads(response.read())

with open("topseller.csv", mode='w') as file:
    data_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for product in data:
        data_writer.writerow([product['name'], product['quantity']])
