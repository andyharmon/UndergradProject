from DataScraper import scrape_tips
from DoClassification import create_classification_file, do_classification
from datetime import datetime

# city_list = ["new york", "chicago", "boston", "san francisco", "los angeles", "las vegas", "philadelphia", "houston",
#             "phoenix", "san antonio", "san diego", "dallas", "san jose"]

city_list = ["new york"]
tip_list = scrape_tips(city_list)

tips_with_ratings = []

for tip in tip_list:
    if tip.rating is not None:
        tips_with_ratings.append(tip)

print('there are ' + str(len(tips_with_ratings)) + ' tips for our total set')

training_set = tips_with_ratings[:len(tips_with_ratings) / 2]
testing_set = tips_with_ratings[len(tips_with_ratings) / 2:]

train_file = create_classification_file(training_set, "training")
test_file = create_classification_file(testing_set, "testing")

do_classification(train_file.name, test_file.name)

print(str(datetime.now().time()) + ": done")
