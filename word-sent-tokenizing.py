from nltk.tokenize import word_tokenize, sent_tokenize

#tokenizing - It is the process of breaking a stream of text up into words, phrases, symbols, or other meaningful elements called tokens.

text = 'Hello, this is the example text. This program uses python and nltk library for natural language processing.'

#seperating words
print(word_tokenize(text))

#seperating sentences
print(sent_tokenize(text))