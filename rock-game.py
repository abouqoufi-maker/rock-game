import random

number_of_choice = int(input("enter the number of choices: "))

x=0

while x < number_of_choice:

    option = ("7ajar", "waraq", "miqas")
    computer = random.choice(option)

    choice = input("enter (7ajar or waraq or miqas): ")
    print(f"your choice is {choice}")
    print(f"robot choice is {computer}")

    if choice == computer:
        number_of_choice+=1
        print("draw! : +1 choice")
    elif choice == "7ajar" and computer == "waraq":
        print("failed !")
    elif choice == "7ajar" and computer == "miqas":
        print("victoitre !")
    elif choice == "waraq" and computer == "7ajar":
        print("victoire !")
    elif choice == "waraq" and computer == "misas":
        print("failed !")
    elif choice == "miqas" and computer == "7ajar":
        print("failed !")
    elif choice == "miqas" and computer == "waraq":
        print("victoire !")
    else:
        pass

    x+=1