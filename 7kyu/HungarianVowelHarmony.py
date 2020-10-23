# -*- coding: utf-8 -*-
def dative(word):
    for letter in word[::-1]:
        if letter in 'eéiíöőüű':
            return word + "nek"
        if letter in 'aáoóuú':
            return word + "nak"
            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # Code almost works, ternary return line is broken/impossible...
def dative(word):
    for l in word[::-1]:
        return word + "nek" if l in 'eéiíöőüű' else word + "nak" if l in 'aáoóuú' else "x" 
            #ternary statement breaks down at last 'else pass', invalid syntax. Can't return pass
            
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

"""
  Vowel harmony is a phenomenon in some languages. It means that "A vowel or vowels in a word are changed to sound the same (thus "in harmony.")" (wikipedia). This kata is based on vowel harmony in Hungarian.
    Task:
  Your goal is to create a function dative() (Dative() in C#) which returns the valid form of a valid Hungarian word w in dative case i. e. append the correct suffix nek or nak to the word w based on vowel harmony rules.

Vowel Harmony Rules (simplified)
  When the last vowel in the word is
      a front vowel (e, é, i, í, ö, ő, ü, ű) the suffix is -nek
      a back vowel (a, á, o, ó, u, ú) the suffix is -nak
Examples:
    dative("ablak") == "ablaknak"
    dative("szék") == "széknek"
    dative("otthon") == "otthonnak"
Preconditions:
    To keep it simple: All words end with a consonant :)
    All strings are unicode strings.
    There are no grammatical exceptions in the tests.
"""
