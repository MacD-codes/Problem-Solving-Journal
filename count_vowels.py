'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.
'''

# SOLUTION
def get_count(sentence):
    count=0
    vowels="aeiou"
    for i in sentence:
        if i in vowels:
            count+=1
    return count