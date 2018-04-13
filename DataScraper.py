from datetime import datetime
import json
import requests

CLIENT_ID = 'TL23INJGO0B40GXYB040G1LXKSQ0JSP5IE010VTWTCHWZEQO'
CLIENT_SECRET = 'UYZWK4UKLKPG2OY54M4MCKMRGVDZJHGRP0OCE5UV44FQF1C5'

city_list = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio",
             "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "San Francisco", "Indianapolis",
             "Columbus", "Fort Worth", "Charlotte", "Detroit", "El Paso", "Seattle", "Denver", "Washington DC",
             "Memphis", "Boston", "Nashville-Davidson", "Baltimore", "Oklahoma City", "Portland", "Las Vegas",
             "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Long Beach", "Kansas City", "Mesa",
             "Atlanta", "Virginia Beach", "Omaha", "Colorado Springs", "Raleigh", "Miami", "Minneapolis", "Oakland",
             "Tulsa", "Cleveland", "Wichita", "New Orleans", "Arlington"]

nyc = ["nyc"]

authorInteractionType = dict(
    liked=1,
    meh=0,
    disliked=-1
)

classifications = dict([(1, "pos"), (-1, "neg"), (0, "meh")])


class Venue:
    def __init__(self, venue_id):
        self.id = venue_id


class Tip:
    def __init__(self, tip_id, tip_text):
        self.id = tip_id
        self.text = tip_text
        self.sentiment = 0
        self.rating = None


def scrape_tips(cities):
    venue_list = get_venues(CLIENT_ID, CLIENT_SECRET, cities)
    tips = []

    for venue in venue_list:
        tips = tips + get_tips(CLIENT_ID, CLIENT_SECRET, venue.id)

    print('there are ' + str(len(tips)) + ' tips')
    return tips


def get_venues(client_id, client_secret, cities):
    venue_list = []
    url = 'https://api.foursquare.com/v2/venues/explore'

    for city in cities:
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
            if "authorInteractionType" in tip:
                new_tip.rating = authorInteractionType[tip["authorInteractionType"]]
            tip_list.append(new_tip)

    print('found ' + str(len(tip_list)) + ' tips for ' + venue_id)
    return tip_list


def create_classification_file(rated_tips, file_class):
    generation_time = datetime.now().strftime("%d%B%Y-%I-%M%p")
    filename = "TextFiles/" + file_class + "-" + generation_time + ".csv"
    skipped_tips = 0
    with open(filename, "w") as text_file:
        for tip in rated_tips:
            try:
                tip_text = str(tip.text).replace(',', '')
                tb_class = classifications[tip.rating]
                text_file.write(tip_text + ',' + tb_class + '\n')
            except UnicodeEncodeError:
                skipped_tips = +1
    print("skipped " + str(skipped_tips) + " tips!")
    return text_file


print(str(datetime.now().time()) + ": start!")
tip_list = scrape_tips(nyc)
tips_with_ratings = []

for tip in tip_list:
    if tip.rating is not None:
        tips_with_ratings.append(tip)

print('there are ' + str(len(tips_with_ratings)) + ' tips for our total set')
data_file = create_classification_file(tips_with_ratings, "data")
print(data_file.name)
print(str(datetime.now().time()) + ": done")
