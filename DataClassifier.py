from DoClassification import do_classification
from datetime import datetime

train_file_name = input("Enter training data filename: ")
test_file_name = input("Enter testing data filename: ")

try:
    do_classification(train_file_name, test_file_name)
    print(str(datetime.now().time()) + ": done")
except IOError:
    print(str(datetime.now().time()) + ": error on filenames, are you sure they are valid filenames?")

