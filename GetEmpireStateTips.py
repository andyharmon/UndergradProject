import json
import requests
from textblob import TextBlob

url = 'https://api.foursquare.com/v2/venues/43695300f964a5208c291fe3/tips'

params = dict(
    client_id='TL23INJGO0B40GXYB040G1LXKSQ0JSP5IE010VTWTCHWZEQO',
    client_secret='UYZWK4UKLKPG2OY54M4MCKMRGVDZJHGRP0OCE5UV44FQF1C5',
    limit=500,
    v=20180125
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

response = data['response']
tips = response['tips']
items = tips['items']
for tip in items:
    tipText = tip['text']
    tipBlob = TextBlob(tipText)
    print(tipText + ": " + str(tipBlob.sentiment.polarity) + '\n')

