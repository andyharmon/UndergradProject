import json
import requests
from Venue import Venue


def getvenues(clientId, clientSecret):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
        client_id=clientId,
        client_secret=clientSecret,
        limit=50,
        near='new york city',
        v=20180125
    )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    venue_list = []
    if data['meta']['code'] == 200:
        items = data['response']['groups'][0]['items']
        for item in items:
            venue_id = item['venue']['id']
            new_venue = Venue(venue_id)
            venue_list.append(new_venue)

    return venue_list
