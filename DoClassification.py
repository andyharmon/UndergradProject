from textblob.classifiers import NaiveBayesClassifier, NLTKClassifier, DecisionTreeClassifier, MaxEntClassifier
from datetime import datetime

classifciations = dict([(1, "pos"), (-1, "neg")])


def create_classification_file(rated_tips, file_class):
    generation_time = datetime.now().strftime("%d%B%Y-%I-%M%p")
    filename = "TextFiles/" + file_class + "-" + generation_time + ".csv"
    skipped_tips = 0
    with open(filename, "w") as text_file:
        for tip in rated_tips:
            # I need to look into how to handle "meh" ratings
            if tip.rating != 0:
                try:
                    tip_text = str(tip.text).replace(',', '')
                    tb_class = classifciations[tip.rating]
                    text_file.write(tip_text + ',' + tb_class + '\n')
                except UnicodeEncodeError:
                    skipped_tips = +1
    print("skipped " + str(skipped_tips) + " tips!")
    return text_file


def do_classification(train_file, test_file):

    with open(train_file) as tips:
        print(str(datetime.now().time()) + ": beginning to train")
        nb_classifier = NaiveBayesClassifier(tips, format="csv")
        print(str(datetime.now().time()) + ": training done")

    with open(test_file) as tips:
        print(str(datetime.now().time()) + ": beginning to test")
        nb_accuracy = nb_classifier.accuracy(tips, format="csv")
        print(str(datetime.now().time()) + ": testing done")
        print("Naive Bayes accuracy: " + str(nb_accuracy))
