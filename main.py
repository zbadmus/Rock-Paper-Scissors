#rock,paper and scissors game
import random
moves=['R','P','S']
print(moves)     
user_choice=input("Enter your move from the list above: ")

#user_choice validation
while True:
    if user_choice != "R" and user_choice != "P" and user_choice != "S":
        print(moves)
        user_choice=input("Enter a valid move from the list above: ")
    else:
        break
CPU_choice = random.choice(moves)
print("Computer's move: ", CPU_choice)

#If there is a tie that is, if player and computer make the same move
while True:
    if user_choice == CPU_choice:
        user_choice=input("Enter your move: ")
    #user_choice validation again
        while True:
            if user_choice != "R" and user_choice != "P" and user_choice != "S":
                print(moves)
                user_choice=input("Enter a valid move from the list above: ")
            else:
                break
        CPU_choice = random.choice(moves)
        print("Computer's move: ", CPU_choice)
    else:
        break
#Determining the winner
if user_choice == "R" and CPU_choice == "P":
        print("Player (Rock):CPU (Paper)")
        print("Oops! Computer wins")
elif user_choice == "P" and CPU_choice == "S":
        print("Player (Paper):CPU (Scissors)")
        print(" Oops! Computer wins")
elif user_choice == "S" and CPU_choice == "R":
        print("Player (Scissors):CPU (Rock)")
        print("Oops! Computer wins")
elif user_choice == "S" and CPU_choice == "P":
        print("Player (Scissors):CPU (Paper)")
        print("Hooray!!! you won!")
elif user_choice == "P" and CPU_choice == "R":
        print("Player (Paper):CPU (Rock)")
        print("Hooray!!! you won!")
elif user_choice == "R" and CPU_choice == "S":
        print("Player (Rock):CPU (Scissors)")
        print("Hooray!!! you won!")