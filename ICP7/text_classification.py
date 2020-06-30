from nltk.corpus import stopwords
from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
import nltk
nltk.download('stopwords')


# Preparing Training Data

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

# Creating TF_IDF instance

tfidf_Vect = TfidfVectorizer()

# Preparing training & testing data using TFIDF transformation

X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)


# Navie Bayes Model training
clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)

# Predicting and calcluating Scores using NB model
clf_predicted = clf.predict(X_test_tfidf)
clf_score = metrics.accuracy_score(twenty_test.target, clf_predicted)
print("Score using NB model - ", clf_score)

# SVM Model training
svm = SVC(kernel='linear', random_state=1)
svm.fit(X_train_tfidf, twenty_train.target)

# Predicting and calcluating Scores using SVM model
svm_predicted = svm.predict(X_test_tfidf)
svm_score = metrics.accuracy_score(twenty_test.target, svm_predicted)
print("Score using SVM - ", svm_score)


# Changing the TFIDF to use Bigram
bigram_tfidf = TfidfVectorizer(ngram_range=(1, 2))

# Preparing testing and training data using Bigram TFIDF
X_train_bigram = bigram_tfidf.fit_transform(twenty_train.data)
X_test_bigram = bigram_tfidf.transform(twenty_test.data)

# Navie Bayes Model training with Bigram TFIDF
bigram_clf = MultinomialNB()
bigram_clf.fit(X_train_bigram, twenty_train.target)

# Predicting with Bigram TFIDF
bigram_clf_predicted = bigram_clf.predict(X_test_bigram)
bigram_clf_score = metrics.accuracy_score(
    twenty_test.target, bigram_clf_predicted)
print("Score using Bigram TFIDF - ", bigram_clf_score)


# TFIDF with argument stop_words='english'
english_tfidf = TfidfVectorizer(stop_words="english")

# Preparing Test and trainng data
X_train_tfidf_english = english_tfidf.fit_transform(twenty_train.data)
X_test_tfidf_english = english_tfidf.transform(twenty_test.data)

# Navie Bayes Model training with TFIDF stopwords english
clf_english = MultinomialNB()
clf_english.fit(X_train_tfidf_english, twenty_train.target)

# Predicting with TFIDF stop words english
clf_english_predicted = clf_english.predict(X_test_tfidf_english)
score = metrics.accuracy_score(twenty_test.target, clf_english_predicted)
print("accuracy score by applying stopword", score)