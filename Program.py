from DataScraper import scrape_tips
from DoClassification import create_classification_file, do_classification

# city_list = ["new york", "chicago", "boston", "san francisco", "los angeles", "las vegas", "philadelphia", "houston",
#             "phoenix", "san antonio", "san diego", "dallas", "san jose"]

city_list = ["new york", "chicago", "boston"]
tip_list = scrape_tips(city_list)

tips_with_ratings = []

for tip in tip_list:
    if tip.rating is not None:
        tips_with_ratings.append(tip)

print('there are ' + str(len(tips_with_ratings)) + ' tips for our training set')
text_file = create_classification_file(tips_with_ratings)
do_classification(text_file.name)
