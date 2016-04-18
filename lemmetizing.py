from nltk.stem import WordNetLemmatizer

# Lemmatizing -

# instance of WordNetLemmatizer
lemmatizer  = WordNetLemmatizer()

words = ['walking', 'googling', 'cheese', 'cats', 'car', 'better']

for i in words:
    print(lemmatizer.lemmatize(i, pos='a'))