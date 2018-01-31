'''
This code calls the API using my client ID and secret and returns the tip
text and sentiment from TextBlob. This code uses the Empire State Building
venue on Foursquare
'''

import json
import requests
from textblob import TextBlob
from Tip import Tip

url = 'https://api.foursquare.com/v2/venues/4af5a46af964a520b5fa21e3/tips'
params = dict(
    client_id='TL23INJGO0B40GXYB040G1LXKSQ0JSP5IE010VTWTCHWZEQO',
    client_secret='UYZWK4UKLKPG2OY54M4MCKMRGVDZJHGRP0OCE5UV44FQF1C5',
    limit=500,
    v=20180125
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

if data['meta']['code'] == 200:
    tipList = []
    tips = data['response']['tips']['items']
    for tip in tips:
        tipText = tip['text']
        # get userInteraction??
        tipSentiment = TextBlob(tipText).sentiment.polarity
        newTip = Tip(tipText, 0, tipSentiment)
        tipList.append(newTip)

print("tipList contains " + str(len(tipList)) + " tips.")
