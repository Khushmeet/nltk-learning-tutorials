from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize


#Stemming - the process for reducing inflected (or sometimes derived) words to their word stem, base or root form—generally a written word form.

ps = PorterStemmer()

words = ['write', 'wrote', 'written', 'writing', 'right']

for w in words:
    print(ps.stem(w))

#for a sentence
text = 'This is an english sentence , which will be tokenized by sent_tokenizer'
sent_words = word_tokenize(text)

#looping through each word
for w in sent_words:
    print(ps.stem(w))