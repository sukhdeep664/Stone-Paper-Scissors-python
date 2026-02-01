import random
"""
1 for Stone
0 for Paper
-1 for Scissors
"""
computer=random.choice([1,0,-1])
user=input("Enter:")
userdict={"s":1,"p":0,"c":-1}
reverse_user={1:"Stone",0:"Paper",-1:"Scissors"}

you=userdict[user]

print("You Chose ",reverse_user[you])
print("Computer Chose",reverse_user[computer])

if(computer==you):
    print("It's a Draw!")
else:
    if(computer==-1 and you==1) :
        print("You win!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Lose")
    elif (computer==1 and you==0):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Lose!")
    elif(computer==0 and you==-1):
        print("You Win!")
    else:
        print("Something Went Wrong!")
            


