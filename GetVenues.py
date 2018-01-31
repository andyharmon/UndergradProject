import json
import requests
from Venue import Venue


def get_venues(client_id, client_secret, city_list):
    venue_list = []
    url = 'https://api.foursquare.com/v2/venues/explore'

    for city in city_list:
        print('Finding venues for ' + city)
        params = dict(
            client_id=client_id,
            client_secret=client_secret,
            limit=50,
            near=city,
            v=20180125
        )

        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        if data['meta']['code'] == 200:
            items = data['response']['groups'][0]['items']
            for item in items:
                venue_id = item['venue']['id']
                new_venue = Venue(venue_id)
                venue_list.append(new_venue)

    return venue_list
