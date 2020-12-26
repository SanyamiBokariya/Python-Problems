from collections import * 

def makeAnagram(a, b):
    frequency_of_characters_in_a = Counter(a)
    frequency_of_characters_in_b = Counter(b)
    c = frequency_of_characters_in_a - frequency_of_characters_in_b
    d = frequency_of_characters_in_b - frequency_of_characters_in_a
    e = c + d
    return len(list(e.elements()))
    
makeAnagram('cde','dcf')
