from TipScraper import scrape_tips
from DoClassification import create_classification_file
from datetime import datetime

city_list = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio",
             "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "San Francisco", "Indianapolis",
             "Columbus", "Fort Worth", "Charlotte", "Detroit", "El Paso", "Seattle", "Denver", "Washington DC",
             "Memphis", "Boston", "Nashville-Davidson", "Baltimore", "Oklahoma City", "Portland", "Las Vegas",
             "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Long Beach", "Kansas City", "Mesa",
             "Atlanta", "Virginia Beach", "Omaha", "Colorado Springs", "Raleigh", "Miami", "Minneapolis", "Oakland",
             "Tulsa", "Cleveland", "Wichita", "New Orleans", "Arlington"]

print(str(datetime.now().time()) + ": start!")

tip_list = scrape_tips(city_list)

tips_with_ratings = []

for tip in tip_list:
    if tip.rating is not None:
        tips_with_ratings.append(tip)

print('there are ' + str(len(tips_with_ratings)) + ' tips for our total set')

data_file = create_classification_file(tips_with_ratings, "data")

print(data_file.name)

print(str(datetime.now().time()) + ": done")
