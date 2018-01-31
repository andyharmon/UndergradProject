from DataScraper import scrape_tips

city_list = ["new york", "chicago", "boston", "san francisco", "los angeles", "las vegas", "philadelphia", "houston"]
tip_list = scrape_tips(city_list)

tips_with_ratings = []
tips_blank_ratings = []

for tip in tip_list:
    if tip.rating is not None:
        tips_with_ratings.append(tip)
    else:
        tips_blank_ratings.append(tip)

print('there are ' + str(len(tips_with_ratings)) + ' tips for our training set')
print('there are ' + str(len(tips_blank_ratings)) + ' tips for our testing set')

