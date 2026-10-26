import random
print("Select the range")
a=int(input("Enter the smaller number"))
b=int(input("Enter the larger number"))
print("Number of attempts to Guess is 5")
num=random.randint(a,b)
attempt=0
while attempt<5:
    n=int(input("Guess the number"))
    if n==num:
        print("YOU WON")
        break
    if n<num:
        print("Guess the higher number")
    else:
        print("Guess the lower number")
    attempt+=1
if attempt==5:
    print(f"You lost TRY AGAIN correct Ans was {num}")