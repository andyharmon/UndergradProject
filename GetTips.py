'''
This code calls the API using my client ID and secret and returns the tip
text and sentiment from TextBlob. This code uses the Empire State Building
venue on Foursquare
'''

import json
import requests
from Tip import Tip

authorInteractionType = dict(
    liked=1,
    meh=0,
    disliked=-1
)


def get_tips(client_id, client_secret, venue_id):

    url = 'https://api.foursquare.com/v2/venues/' + venue_id + '/tips'
    params = dict(
        client_id=client_id,
        client_secret=client_secret,
        limit=500,
        v=20180125
    )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    tip_list = []

    if data['meta']['code'] == 200:
        tips = data['response']['tips']['items']
        for tip in tips:
            tip_text = tip['text']
            tip_id = tip['id']
            new_tip = Tip(tip_id, tip_text)
            tip_list.append(new_tip)

    print('found ' + str(len(tip_list)) + ' tips for ' + venue_id)
    return tip_list
