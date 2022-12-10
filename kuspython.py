u = 0
c = 0
import random
for i in range(10000):
    user_choice = input("chose num between 1 to 6: ")
    if user_choice!="exit":
       user_choice=int(user_choice)
       cpu_choice = int(random.randint(1, 6))
       print("cpu_choice= ", cpu_choice)
       if user_choice==cpu_choice:
            u=u+1
            print("win")
        elif user_choice!=cpu_choice:
            print("loss")
            c=c+1
    elif user_choice=='exit':
        print("Final Scores")
        print("CPU score:",c)
        print("User score:",u)
        if c>u:
            print("cpu won the game")
        elif c<u:
            print("user won the game")
        else:
            print("Tie")