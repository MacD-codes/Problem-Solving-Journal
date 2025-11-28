str1="hello"
rev_str=""
for i in range(len(str1)-1,-1,-1):
    rev_str+=str1[i]

print(rev_str)

# short cut
print("hello"[::-1])