"""
Import the string library.
Create a variable alphabet that consists of the lowercase and uppercase letters
in the English alphabet using the ascii_letters attribute of the string library.

"""

# Write your code here!
import string

alphabet = string.ascii_letters

#EXERCISE 1B

"""

The lower and upper cases of the English alphabet is stored as alphabet.
Consider the sentence
'Jim quickly realized that the beautiful gowns are expensive'.
Create a dictionary count_letters with keys consisting of each unique
letter in the sentence and values consisting of the number of times each
letter is used in this sentence.
Count both upper case and lower case letters separately in the dictionary.

"""

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
#write your code here!
count = 0

for letter in sentence:
    
    if letter in alphabet:
        
        if letter in count_letters:
            
            count_letters[letter] += 1

        else:
            
            count_letters[letter] = 1
