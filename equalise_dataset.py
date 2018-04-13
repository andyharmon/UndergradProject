import Tkinter as tk
from tkFileDialog import askopenfilename
import csv
from random import sample

root = tk.Tk()
root.withdraw()

data_file_name = askopenfilename(title="Select data file")

num_of_items = 655

pos_reviews = list()
neg_reviews = list()
# meh_reviews = list()

with open(data_file_name, 'rb') as f:
    reader = csv.reader(f)
    reader_output = map(tuple, reader)

for review in reader_output:
    if review[1] == "pos":
        pos_reviews.append(review)
    if review[1] == "neg":
        neg_reviews.append(review)
    # if review[1] == "meh":
    #     meh_reviews.append(review)

pos_reviews = sample(pos_reviews, len(pos_reviews))
neg_reviews = sample(neg_reviews, len(neg_reviews))
# meh_reviews = sample(meh_reviews, len(meh_reviews))

file_reviews = list(pos_reviews[:num_of_items] + neg_reviews[:num_of_items])  # + meh_reviews[:num_of_items])
file_reviews = sample(file_reviews, len(file_reviews))

filename = "TextFiles/equalised_data_OnlyPosAndNeg.csv"
with open(filename, "w") as text_file:
    for review in file_reviews:
        text_file.write(str(review[0]) + "," + str(review[1]) + '\n')
