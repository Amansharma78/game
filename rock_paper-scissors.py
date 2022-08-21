import random
lst = ["r" , "p", "s"]

num=0
count_c = 0
count_u = 0
while(num<10):
    num+=1
    a = random.choice(lst)
    print ("******** No. of chances left :",10-num,"********")
    c= input("--------Enter r for rock p for paper and s for scissors--------\n")
    if (a=="r" and c=="r") or (a=="p" and c=="p") or(a=="s" and c=="s"):
        print("tie!")
    elif (a=="r" and c=="s") or (a=="s" and c=="p") or (a=="p" and c=="r"):
        print("You lost!")
        count_c+=1
    else:
        print("You won!")
        count_u+=1
    if a=="r":
        print("Computer chosen Rock")
    if a=="s":
        print("Computer chosen Scissors")
    if a=="p":
        print("Computer chosen Paper")
if count_c<count_u:
    print("You are winner!")
elif count_c==count_u:
    print("Game Tie")
else:
    print("You are losser!")
    