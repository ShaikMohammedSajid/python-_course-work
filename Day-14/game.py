import random
computer = random.choice([1,-1,0])
youstr =input("Enter Your Choise: ")
youdict = {"s" :1,"w" :-1 , "g":0}
reversedict = {1:"sanke",-1:"water",0:"gun"}
you = youdict[youstr]
print(f"Your Choise is :{reversedict[you]}")
print(f"Coumputer Choise is :{reversedict[computer]}")
if computer == you:
    print("It's a draw")

elif computer == 1 and you == -1:
    print("You lose")

elif computer == 1 and you == 0:
    print("You win")

elif computer == -1 and you == 1:
    print("You win")

elif computer == -1 and you == 0:
    print("You lose")

elif computer == 0 and you == 1:
    print("You lose")

elif computer == 0 and you == -1:
    print("You win")

else:
    print("Something went wrong")
