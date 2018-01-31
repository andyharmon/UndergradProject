import json
import requests
from Venue import Venue

url = 'https://api.foursquare.com/v2/venues/explore'
params = dict(
    client_id='TL23INJGO0B40GXYB040G1LXKSQ0JSP5IE010VTWTCHWZEQO',
    client_secret='UYZWK4UKLKPG2OY54M4MCKMRGVDZJHGRP0OCE5UV44FQF1C5',
    limit=50,
    near='new york city',
    v=20180125
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

venueList = []
if data['meta']['code'] == 200:
    items = data['response']['groups'][0]['items']
    for item in items:
        venueId = item['venue']['id']
        newVenue = Venue(venueId)
        venueList.append(newVenue)

print('Found ' + str(len(venueList)) + ' venues')
