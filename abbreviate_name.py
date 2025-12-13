'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
'''

# SOLUTION
def abbrev_name(name):
    word=name.split(" ")
    first=word[0][0].upper()
    second=word[1][0].upper()
    
    return f"{first}.{second}"
    