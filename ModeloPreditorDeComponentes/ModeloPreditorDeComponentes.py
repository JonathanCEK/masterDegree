import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer #vectorizador
from sklearn.feature_selection import SelectKBest, chi2 # seletor de melhores atributos
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score #reporte de resultados
from sklearn.model_selection import GridSearchCV, cross_val_predict #crossvalidation
from sklearn.svm import SVC #SVM
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split #divisão teste e treino
from scipy.sparse import csr_matrix
import joblib


def predizerComponentes (string2Vet_G): 
    configuraçõesClassificador = getClassifierConfig("Navigation bar")
    print("Navigation bar - "+str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))

    configuraçõesClassificador = getClassifierConfig("Bottom app bar")
    print("Bottom app bar - "+str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))

    configuraçõesClassificador = getClassifierConfig("Top app bar")
    print("Top app bar - "+str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))

    configuraçõesClassificador = getClassifierConfig("Sound effects")
    print("Sound effects - " +str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))

    configuraçõesClassificador = getClassifierConfig("Navigation drawer")
    print("Navigation drawer - "+str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))

    configuraçõesClassificador = getClassifierConfig("Primary tab")
    print("Primary tab - "+str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))

    configuraçõesClassificador = getClassifierConfig("Social interaction")
    print("Social interaction - "+str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))

    configuraçõesClassificador = getClassifierConfig("Account required")
    print("Account required - "+str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))

    configuraçõesClassificador = getClassifierConfig("Card list")
    print("Card list - "+str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))


    configuraçõesClassificador = getClassifierConfig("Map view")
    print("Map view - "+str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))

    configuraçõesClassificador = getClassifierConfig("Videos")
    print("Videos - "+str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))

    configuraçõesClassificador = getClassifierConfig("Text field")
    print("Text field - "+str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))


    configuraçõesClassificador = getClassifierConfig("Landscape mode")
    print("Landscape mode - " +str(obterClassification(configuraçõesClassificador[0], configuraçõesClassificador[1], configuraçõesClassificador[2], configuraçõesClassificador[3], string2Vet_G)))

def getClassifierConfig(nomeAtributo):

  loaded_variables = joblib.load(nomeAtributo+'Var.pkl')
  analyzerType_G = loaded_variables['analyzerType_G']
  ngramRange_G = loaded_variables['ngramRange_G']
  palavras_selecionadas_G = loaded_variables['palavras_selecionadas_G']
  clf_G = loaded_variables['clf_G']

  #analyzerType_G = 'word'
  #ngramRange_G = (1, 3)
  #clf_G = retornoCriarFiles[1]
  #clf_G = joblib.load('multinomial_nb_classifier.pkl')
  #palavras_selecionadas_G = retornoCriarFiles[0]


  return [analyzerType_G, ngramRange_G, clf_G, palavras_selecionadas_G]

def stringVectorizer(analyzerType, ngramRange, string2Vet):

  vectorizer2 = CountVectorizer(analyzer=analyzerType, ngram_range=ngramRange)

  X_total2 = vectorizer2.fit_transform([string2Vet])

  palavras_novas = vectorizer2.get_feature_names_out()

  return [X_total2, palavras_novas]

def sparseMatrixTransform(new_words, selected_words, sparse_matrix_data):

  # Find common words
  common_words = set(new_words).intersection(selected_words)

  # Create mapping of common words to column indices
  common_word_indices = {word: index for index, word in enumerate(selected_words) if word in common_words}

  # Create new sparse matrix with integer values
  row_indices = np.zeros(len(common_word_indices))
  column_indices = np.array([common_word_indices[word] for word in common_words])
  data = np.array([sparse_matrix_data[(0, np.where(np.array(new_words) == word)[0][0])] for word in common_words])

  return csr_matrix((data, (row_indices, column_indices)), shape=(1, len(selected_words)))


def predictThis(clf, X):
  return clf.predict(X)[0]

#Inserir a descrição do aplicativo na string abaixo. Lembre-se de importar todos os classificadores anteriormente
AppDescription = '''Whether you’re looking for a spark of inspiration with reels or want to dive deeper into something you already love with Marketplace or in groups, you can discover ideas, experiences and people that fuel your interests and help you make progress on the things that matter to you on Facebook.

Explore and expand your interests:
* Shop for affordable and uncommon stuff on Marketplace and take your hobbies to the next level
* Personalize your Feed to see more of what you like, less of what you don’t
* Watch reels for quick entertainment that sparks inspiration
* Discover creators, small businesses and communities who can help you dive deeper into the things you care about

Connect with people and communities:
* Join groups to learn tips and tricks from real people who’ve been there, done that
* Catch up with friends, family and influencers through Feed and stories

Share your world:
* Effortlessly create reels from trending templates, or let your creativity shine with a full suite of editing tools
* Customize your profile to choose how you show up and who you share your posts with
* Turn your hobby into a side hustle by becoming a creator or selling things on Marketplace
* Celebrate everyday, candid moments with stories, which disappear in 24 hours

Consumer Health Privacy Policy: https://www.facebook.com/privacy/policies/health'''

predizerComponentes(AppDescription)