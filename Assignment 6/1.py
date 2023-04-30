import sys
from sklearn import svm
from random import shuffle


def unzip(dataset):
    dataset = list(zip(*dataset))
    return dataset[0], dataset[1]


def import_data(filename):
    x = []
    y = []
    ifile = open(filename, 'r')
    for line in ifile:
        line = line.strip('\n')
        data = line.split(',')
        x.append(data[:-1])
        y.append(data[-1])
    ifile.close()
    dataset = list(zip(x, y))
    return dataset


def create_sets(dataset, train_percent):
    shuffle(dataset)
    training_set = dataset[:int(len(dataset) * train_percent)]
    testing_set = dataset[int(len(dataset) * train_percent):]
    return training_set, testing_set


def train_model(training_set, kernel, c):
    x, y = unzip(training_set)
    if kernel == 'quad':
        kernel = 'poly'
    clf = svm.SVC(kernel=kernel, degree=2, C=c)
    clf.fit(x, y)
    return clf


def find_accuracy(testing_set, clf):
    x, y = unzip(testing_set)
    predictions = clf.predict(x)
    correct = 0
    for i in range(len(predictions)):
        if predictions[i] == y[i]:
            correct += 1
    return (correct / len(predictions)) * 100


def svf(kernel, c):
    global training_set, testing_set
    # Train model
    clf = train_model(training_set, kernel, c)
    # Find accuracy
    accuracy_test = find_accuracy(testing_set, clf)
    accuracy_train = find_accuracy(training_set, clf)
    return accuracy_test, accuracy_train


def main(C=1):
    global training_set, testing_set
    # Import data
    dataset = import_data(sys.argv[1])
    # Create training and testing sets
    training_set, testing_set = create_sets(dataset, 0.7)

    print("Training the SVM models, please wait this may take a few minutes...")
    tasks = [('linear', C), ('quad', C), ('rbf', C)]
    accuracies = []
    for kernel, c in tasks:
        accuracy_test, accuracy_train = svf(kernel, c)
        accuracies.append((accuracy_test, accuracy_train))
    print(f"Kernel\tC\tTest Accuracy\t\tTrain Accuracy")
    for kernel, c in tasks:
        print(f'{kernel}\t{c}\t{accuracies[tasks.index((kernel, c))][0]}\t{accuracies[tasks.index((kernel, c))][1]}')

if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print('Usage: python3 1.py <filename> [C]')
        sys.exit(1)
    if len(sys.argv) == 3:
        main(float(sys.argv[2]))
    else:
        main()
