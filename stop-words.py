from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Stop Words - are words which are filtered out before or after processing of natural language data.

text = 'This is the nltk library, which stands for natural langauge toolkit.'

#set of stop words as specified by nltk
stop_words = set(stopwords.words('english'))
w_tokens = word_tokenize(text)

sentence = []

#filtering the stop words from tokens list
for token in w_tokens:
    if token not in stop_words:
        sentence.append(token)

print(sentence)
