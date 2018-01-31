class Tip:
    def __init__(self, tip_id, tip_text):
        self.id = tip_id
        self.text = tip_text
        self.sentiment = 0
        self.rating = 0

    def set_sentiment(self, sentiment):
        self.sentiment = sentiment

    def set_rating(self, rating):
        self.rating = rating