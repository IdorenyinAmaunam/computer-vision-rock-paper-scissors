import random
import string
import cv2
from keras.models import load_model
import numpy as np
import time

class Rock_paper_scissors:

    def get_computer_choice(self):
        choice_list = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choice_list)
        print(computer_choice)

        return computer_choice


    def play_game(self):

        
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        winner_count = 0
        start_time = time.time()
        while True: 
            
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)

            user_choice = self.get_prediction(prediction)
            computer_choice = self.get_computer_choice()

            winner = self.get_winner(computer_choice, user_choice)
            if (winner == "Congratulations, you won!"):
                winner_count += 1

            cv2.imshow('frame', frame)

            # Press q to close the window
            print(prediction)

            max_view = np.max(prediction)
            max_view = time.time()
            print(max_view)
            
            current_time = time.time()
            period = current_time-start_time
    
            if cv2.waitKey(1) & 0xFF == ord('q') or (period > 10) or \
                (winner_count >= 3): 
                break
                return user_choice

        return (max_view, period)

    def get_prediction(self, prediction):
        predict_index = np.argmax(prediction)
        if(predict_index == 0):
            user_choice = "rock"
        elif(predict_index == 1):
            user_choice = "paper"
        else:
            user_choice = "scissors"
                
        return(user_choice)

    
    #def countdown_timer(self):
    #    start_time = time.time()

    ##    current_time = time.time()
    #    period = current_time - start_time

    #   return period
    
    def get_winner(self, computer_choice, user_choice):
        print("\nYou choose: ", user_choice)
        print("The computer choose: ", computer_choice,"\n")

        if computer_choice == user_choice:
            print("Its a tie, Please, play again")

        elif (computer_choice == "scissors" and user_choice == "rock") or \
            (computer_choice == "rock" and user_choice == "paper") or \
        (   computer_choice == "paper" and user_choice == "scissors"):
            print("Congratulations, you won!")
            
        else:
            print("You lost")



rps_obj = Rock_paper_scissors()
computer_choice = rps_obj.get_computer_choice()
user_choice = rps_obj.play_game()
rps_obj.get_winner(computer_choice, user_choice)
#rps_obj.get_winner()

#retrived = [rps_obj.get_prediction()]
#user_choice = retrived[0]
#period = retrived[-1]

#time.time(user_choice, 0.0)
#rps_obj.get_winner(computer_choice, user_choice)
#print ("The time it took is: ", period)
#user_choice = play.get_user_choice()computer_choice
#play.get_winner(computer_choice, user_choice)
