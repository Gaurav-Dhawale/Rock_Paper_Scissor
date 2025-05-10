import random
def game():
    while True:
        #Preamble & Rules
        print("***  Welcome To The Game  ***")
        print("For the unfamiliar \n"
              "Rock vs Paper ==> Paper Wins!\n"
              "Rock vs Scissor ==> Rock Wins!\n"
              "Paper vs Scissor ==> Scissor Wins!\n\n")

        # Player Turn
        print("***   Player Turn   ***\n"
              "Enter your choice: \n"
              "1-Rock\n"
              "2-Paper\n"
              "3-Scissor")

        p_choice=int(input("Enter Your Choice: "))
        while p_choice>3 or p_choice<1:
            choice=int(input("Enter a valid Choice: "))

        if p_choice==1:
            p_choice_name="Rock"
        elif p_choice==2:
            p_choice_name="Paper"
        else:
            p_choice_name="Scissor"

        print("Your Choice is : ",p_choice_name)


        # Computer Turn
        print("\n\n***   Computer's Turn   ***")

        c_choice=random.randint(1,3)
        if c_choice==1:
            c_choice_name="Rock"
        elif c_choice==2:
            c_choice_name="Paper"
        else:
            c_choice_name="Scissor"

        print("Computer Choice is : ", c_choice_name)


        # Result

        print("\nIt Is",p_choice_name, "vs", c_choice_name)


        if p_choice==c_choice:
            print("\n***   Its a tie   ***\n")
        elif (p_choice==1 and c_choice==2) or (p_choice==2 and c_choice==3) or (p_choice==3 and c_choice==1):
            print("\n***   Computer Wins   ***\n")
        else:
            print("\n***   Player Wins   ***\n")

        p_again = input("Do you want to play again?\n "
                        "Press y to play again\n"
                        "press n to exit\n")

        if p_again == 'y':
            game()
        elif p_again == 'n':
            print("***   Thank you for playing   ***")


        break


game()

