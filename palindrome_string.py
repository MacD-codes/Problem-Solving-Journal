str1="aba"
rev_str=""
for i in range(len(str1)-1,-1,-1):
    rev_str+=str1[i]

if rev_str==str1:
    print(str1,"is palindrome")
else:
    print("It is not palindrome")