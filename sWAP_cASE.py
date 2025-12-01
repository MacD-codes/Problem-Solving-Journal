'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
'''

# Solution:
def swap_case(s):

    modified_str=""
    for i in s:
        if i.islower()==True:
            modified_str+=i.upper()
        elif i.isupper()==True:
            modified_str+=i.lower()
        else:
            modified_str+=i
    return modified_str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
