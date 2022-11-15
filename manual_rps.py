import random
import string

class Rock_paper_scissors:
    


    def get_computer_choice(self):
        choice_list = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choice_list)
        print(computer_choice)

        return computer_choice


    def get_user_choice(self):
        print ("Rock-Scissors-Paper_Game")
        user_choice = input("Choose a word from: \n Rock \n Scissors \n Paper: ")

        return user_choice
    
    def get_winner(self, computer_choice, user_choice):
        print("\nYou choose: ", user_choice)
        print("The computer choose: ", computer_choice,"\n")

        if computer_choice == user_choice:
            print("Its a tie, Please, play again")

        elif (computer_choice == "scissors" and user_choice == "rock") or \
            (computer_choice == "rock" and user_choice == "paper") or \
            (computer_choice == "paper" and user_choice == "scissors"):
            print("Congratulations, you won!")
        else:
            print("You lost")
                   

rps_obj = Rock_paper_scissors()
computer_choice = rps_obj.get_computer_choice()
user_choice = rps_obj.get_user_choice()
rps_obj.get_winner(computer_choice, user_choice)

#user_choice = play.get_user_choice()computer_choice
#play.get_winner(computer_choice, user_choice)
