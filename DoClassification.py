from datetime import datetime
import csv
import nltk

classifications = dict([(1, "pos"), (-1, "neg")])


def create_classification_file(rated_tips, file_class):
    generation_time = datetime.now().strftime("%d%B%Y-%I-%M%p")
    filename = "TextFiles/" + file_class + "-" + generation_time + ".csv"
    skipped_tips = 0
    with open(filename, "w") as text_file:
        for tip in rated_tips:
            if tip.rating != 0:
                try:
                    tip_text = str(tip.text).replace(',', '')
                    tb_class = classifications[tip.rating]
                    text_file.write(tip_text + ',' + tb_class + '\n')
                except UnicodeEncodeError:
                    skipped_tips = +1
    print("skipped " + str(skipped_tips) + " tips!")
    return text_file


def document(tips_file):
    with open(tips_file, 'rb') as f:
        reader = csv.reader(f)
        reader_output = map(tuple, reader)

    document_list = list()

    for item in reader_output:
        document_list.append((item[0].split(' '), item[1]))

    return document_list


def tokenize_document(document):
    document_string = ""
    for item in document:
        document_string += str(item[0])

    return nltk.tokenize.word_tokenize(document_string)


def document_features(document, word_features):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains{}'.format(word)] = (word in document_words)
    return features


def do_classification(data_file):

    print("creating document file")
    data_document = document(data_file)

    print("creating document feature set")
    data_tokens = tokenize_document(data_document)
    all_training_words = nltk.FreqDist(w.lower() for w in data_tokens)
    word_features = list(all_training_words)[:2000]
    featureset = [(document_features(d, word_features), c) for (d, c) in data_document]

    print("creating training and testing set")
    train_set, test_set = featureset[:len(data_document) / 2], featureset[len(data_document) / 2:]

    print("beginning training")
    print("Naive Bayes")
    nb_classifier = nltk.NaiveBayesClassifier.train(train_set)
    print("Decision Tree")
    dt_classifier = nltk.DecisionTreeClassifier.train(train_set)
    print("Max Entropy")
    me_classifier = nltk.MaxentClassifier.train(train_set)

    print("beginning testing")
    generation_time = datetime.now().strftime("%d%B%Y-%I-%M%p")
    filename = "Outputs/" + generation_time + ".txt"

    with open(filename, "w") as output_file:
        output_file.write("Naive Bayes accuracy: " + str(nltk.classify.accuracy(nb_classifier, test_set)) + '\n')
        output_file.write("Decision Tree accuracy: " + str(nltk.classify.accuracy(dt_classifier, test_set)) + '\n')
        print(dt_classifier.pseudocode())
        output_file.write("Maximum Entropy accuracy: " + str(nltk.classify.accuracy(me_classifier, test_set)) + '\n')

    print("done!")
