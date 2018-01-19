#Liam Collins
#1/18/18
#stringAnalysis.py - Characters, Numbers, Words

sentence = input('Enter a sentence: ')

words = sentence.split()
#print(len(words))
characters = len(sentence)
#print(characters)

space = ' '
number_of_space = sentence.count(space)
letters = len(sentence)-number_of_space
#print(letters)
print('Your sentence has', len(words), 'words,', characters, 'characters and', letters, 'letters')

SENTENCE = sentence.upper()
charSearch = input('Enter a character to search for: ')
print('Your sentence has', SENTENCE.count(charSearch.upper()), 'of the character', charSearch)

wordSearch = input('Enter a word to search for: ')
print('Your Sentence has', SENTENCE.count(wordSearch.upper()), 'of the word', wordSearch)