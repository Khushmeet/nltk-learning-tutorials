from nltk.corpus import wordnet

# WordNet -
# Synsets -

# Getting synsets of word program
print(wordnet.synsets('program'))

# Getting name of 3rd synset of word nucleus
print(wordnet.synsets('nucleus')[3].name())

# Getting name of lemma of word computer
print(wordnet.synsets('computer')[0].lemmas()[1].name())

# Getting definition of the word software
print(wordnet.synsets('software')[0].definition())

# Getting the examples of the word python
print(wordnet.synsets('nucleus')[0].examples())
