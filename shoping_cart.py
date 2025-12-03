foods=[]
prices=[]
total=0

while True:
    f=input("Enter the food to cart (q to quit) : ")
    if f.lower()=="q":
        break
    else:
        p=float(input(f"Enter the price of {f}: Rs."))
        foods.append(f)
        prices.append(p)

print("     ----- YOUR CART -----       ")

for f in foods:
    print(f)
for p in prices:
    total+=p

print(f"Your total is: Rs.{total}")
    

