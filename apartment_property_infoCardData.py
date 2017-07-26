import requests
import json
from bs4 import BeautifulSoup


infoCardHeaders = {'accept' : 'application/json, text/javascript, */*; q=0.01',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-US,en;q=0.8',
'content-type':'application/json',
'origin':'https://www.apartments.com',
'referer':'https://www.apartments.com/',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
'x-requested-with':'XMLHttpRequest'}

def getInfo(listingID):
	'''Takes a string, listingID, and returns the infoCardData for that ID.'''
	payload = {"ListingKeys":[listingID],"SearchCriteria":{}}
	req = requests.post('https://www.apartments.com/services/property/infoCardData', headers=infoCardHeaders, json=payload)
	#return req.json()
	return req


def parseInfo(infoJSON):
	'''Takes an infoJSON and returns desired values in tuple form.'''
	name = infoJSON['PropertyName']
	url = infoJSON['PropertyUrl']
	rating = infoJSON['Listing']['Rating']
	latitude = infoJSON['Listing']['Address']['Location']['Latitude']
	longitude = infoJSON['Listing']['Address']['Location']['Longitude']