from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import  accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import  accuracy_score, precision_score, recall_score, f1_score


def porownywarka_klasyfiaktorow(X_train_bow, X_test_bow, y_train, y_test):


    # Inicjalizuj klasyfikatory
    naive_bayes = MultinomialNB()
    svm = SVC()
    logistic_regression = LogisticRegression()
    knn = KNeighborsClassifier()
    decision_tree = DecisionTreeClassifier()
    random_forest = RandomForestClassifier()

    # Trenuj klasyfikatory
    naive_bayes.fit(X_train_bow, y_train)
    svm.fit(X_train_bow, y_train)
    logistic_regression.fit(X_train_bow, y_train)
    knn.fit(X_train_bow, y_train)
    decision_tree.fit(X_train_bow, y_train)
    random_forest.fit(X_train_bow, y_train)

    # Dokonaj predykcji na zbiorze testowym
    predictions_naive_bayes = naive_bayes.predict(X_test_bow)
    predictions_svm = svm.predict(X_test_bow)
    predictions_logistic_regression = logistic_regression.predict(X_test_bow)
    predictions_knn = knn.predict(X_test_bow)
    predictions_decision_tree = decision_tree.predict(X_test_bow)
    predictions_random_forest = random_forest.predict(X_test_bow)

    # Miary jakości
    accuracy_naive_bayes = accuracy_score(y_test, predictions_naive_bayes)
    accuracy_svm = accuracy_score(y_test, predictions_svm)
    accuracy_logistic_regression = accuracy_score(y_test, predictions_logistic_regression)
    accuracy_knn = accuracy_score(y_test, predictions_knn)
    accuracy_decision_tree = accuracy_score(y_test, predictions_decision_tree)
    accuracy_random_forest = accuracy_score(y_test, predictions_random_forest)

    precision_naive_bayes = precision_score(y_test, predictions_naive_bayes, average='weighted')
    precision_svm = precision_score(y_test, predictions_svm, average='weighted')
    precision_logistic_regression = precision_score(y_test, predictions_logistic_regression, average='weighted')
    precision_knn = precision_score(y_test, predictions_knn, average='weighted')
    precision_decision_tree = precision_score(y_test, predictions_decision_tree, average='weighted')
    precision_random_forest = precision_score(y_test, predictions_random_forest, average='weighted')

    recall_naive_bayes = recall_score(y_test, predictions_naive_bayes, average='weighted')
    recall_svm = recall_score(y_test, predictions_svm, average='weighted')
    recall_logistic_regression = recall_score(y_test, predictions_logistic_regression, average='weighted')
    recall_knn = recall_score(y_test, predictions_knn, average='weighted')
    recall_decision_tree = recall_score(y_test, predictions_decision_tree, average='weighted')
    recall_random_forest = recall_score(y_test, predictions_random_forest, average='weighted')

    f1_naive_bayes = f1_score(y_test, predictions_naive_bayes, average='weighted')
    f1_svm = f1_score(y_test, predictions_svm, average='weighted')
    f1_logistic_regression = f1_score(y_test, predictions_logistic_regression, average='weighted')
    f1_knn = f1_score(y_test, predictions_knn, average='weighted')
    f1_decision_tree = f1_score(y_test, predictions_decision_tree, average='weighted')
    f1_random_forest = f1_score(y_test, predictions_random_forest, average='weighted')

    slowiczek = {"Dokladnosc": {}, "Precyzja": {}, "Czulosc": {}, "F1-Score": {}}
    slowiczek["Dokladnosc"]["Naive Bayes"] = accuracy_naive_bayes
    slowiczek["Dokladnosc"]["SVM"] = accuracy_svm
    slowiczek["Dokladnosc"]["SVM"] = accuracy_svm
    slowiczek["Dokladnosc"]["Logistic Regression"] = accuracy_logistic_regression
    slowiczek["Dokladnosc"]["KNN"] = accuracy_knn
    slowiczek["Dokladnosc"]["Decision Tree"] = accuracy_decision_tree
    slowiczek["Dokladnosc"]["Random Forest"] = accuracy_random_forest

    slowiczek["Precyzja"]["Naive Bayes"] = precision_naive_bayes
    slowiczek["Precyzja"]["SVM"] = precision_svm
    slowiczek["Precyzja"]["Logistic Regression"] = precision_logistic_regression
    slowiczek["Precyzja"]["KNN"] = precision_knn
    slowiczek["Precyzja"]["Decision Tree"] = precision_decision_tree
    slowiczek["Precyzja"]["Random Forest"] = precision_random_forest

    slowiczek["Czulosc"]["Naive Bayes"] = recall_naive_bayes
    slowiczek["Czulosc"]["SVM"] = recall_svm
    slowiczek["Czulosc"]["Logistic Regression"] = recall_logistic_regression
    slowiczek["Czulosc"]["KNN"] = recall_knn
    slowiczek["Czulosc"]["Decision Tree"] = recall_decision_tree
    slowiczek["Czulosc"]["Random Forest"] = recall_random_forest

    slowiczek["F1-Score"]["Naive Bayes"] = f1_naive_bayes
    slowiczek["F1-Score"]["SVM"] = f1_svm
    slowiczek["F1-Score"]["Logistic Regression"] = f1_logistic_regression
    slowiczek["F1-Score"]["KNN"] = f1_knn
    slowiczek["F1-Score"]["Decision Tree"] = f1_decision_tree
    slowiczek["F1-Score"]["Random Forest"] = f1_random_forest

    return slowiczek

def tylko_svm(X_train_bow, X_test_bow, y_train, y_test):
    svm = SVC()
    svm.fit(X_train_bow, y_train)
    predictions_svm = svm.predict(X_test_bow)
    accuracy_svm = accuracy_score(y_test, predictions_svm)
    precision_svm = precision_score(y_test, predictions_svm, average='weighted')
    recall_svm = recall_score(y_test, predictions_svm, average='weighted')
    slowiczek = {"Dokladnosc": {}, "Precyzja": {}, "Czulosc": {}, "F1-Score": {}}