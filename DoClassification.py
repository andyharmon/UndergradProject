from datetime import datetime
import csv
import nltk


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


def document_features(doc, word_features):
    document_words = set(doc)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features


def do_classification(data_file):

    print("creating document file")
    data_document = document(data_file)

    print("creating document feature set")
    data_tokens = tokenize_document(data_document)
    all_training_words = nltk.FreqDist(w.lower() for w in data_tokens)
    word_features = list(all_training_words)[:2000]
    feature_set = [(document_features(d, word_features), c) for (d, c) in data_document]

    print("creating training and testing set")
    test_set, train_set = feature_set[:len(data_document) / 2], feature_set[len(data_document) / 2:]

    print("beginning training")
    print("Naive Bayes")
    nb_classifier = nltk.NaiveBayesClassifier.train(train_set)
    nb_classifier.show_most_informative_features(10)
    print("Decision Tree")
    dt_classifier = nltk.DecisionTreeClassifier.train(train_set)
    print(dt_classifier.pseudocode())
    print("Max Entropy")
    me_classifier = nltk.MaxentClassifier.train(train_set, algorithm="gis", max_iter=10)
    me_classifier.show_most_informative_features(10)

    print("beginning testing")
    generation_time = datetime.now().strftime("%d%B%Y-%I-%M%p")
    filename = "Outputs/" + generation_time + ".txt"

    nb_accuracy = nltk.classify.accuracy(nb_classifier, test_set)
    dt_accuracy = nltk.classify.accuracy(dt_classifier, test_set)
    me_accuracy = nltk.classify.accuracy(me_classifier, test_set)

    with open(filename, "w") as output_file:
        output_file.write("Naive Bayes accuracy: " + str(nb_accuracy) + '\n')
        output_file.write("Decision Tree accuracy: " + str(dt_accuracy) + '\n')
        output_file.write("Maximum Entropy accuracy: " + str(me_accuracy) + '\n')

    print("done!")

