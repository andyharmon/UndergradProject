from textblob.classifiers import NaiveBayesClassifier, NLTKClassifier
import datetime

classifciations = dict([(1, "pos"), (-1, "neg")])
nb_classifier = None


def create_classification_file(rated_tips):
    classification_time = datetime.datetime.now().strftime("%d%B%Y-%I-%M%p")
    filename = "TextFiles/textfile-" + classification_time + ".csv"
    with open(filename, "w") as text_file:
        for tip in rated_tips:
            # I need to look into how to handle "meh" ratings
            if tip.rating != 0:
                try:
                    tip_text = str(tip.text)
                    tip_text = tip_text.strip(',')
                    tb_class = classifciations[tip.rating]
                    text_file.write(tip_text + ',' + tb_class + '\n')
                except UnicodeEncodeError:
                    print("error found on tip with text: " + tip.text)
    return text_file


def do_classification(text_file_name):
    with open(text_file_name) as tips:
        nb_classifier = NaiveBayesClassifier(tips, format="csv")
        prob_dist = nb_classifier.classify("I enjoyed the tacos")
        print(str(prob_dist.max))

