import random

exit = False

user_scores = 0
computer_scores = 0

while exit == False:
    choices = ["rock", "paper", "scissors"]
    print()
    user_input = input("Select rock | paper | scissors | exit: ")
        
    print()
    computer_input = random.choice(choices)
    
    if user_input == "exit":
        print("Game ended")
        exit = True
        print("Your total score: "+str(user_scores))
        print("Computer total score: "+str(computer_scores))
        if user_scores > computer_scores:
            print ("Congratulation! You won the game.")
        elif computer_scores > user_scores:
            print("Computer won! Better luck next time.")
        else:
            print("It's a tie")
        
        
    elif user_input == "rock":
        if computer_input == "rock":
            print("Your input: rock")
            print("Computer input: rock")
            print("It's a tie!")
            
        elif computer_input == "scissors":
            print("Your input: rock")
            print("Computer input: scissors")
            print("You win!")
            user_scores += 1
            
        elif computer_input == "paper":
            print("Your input: rock")
            print("Computer input: paper")
            print("Computer wins!")
            computer_scores += 1
            
            
    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input: paper")
            print("Computer input: rock")
            print("You win!")
            user_scores += 1
            
        elif computer_input == "scissors":
            print("Your input: paper")
            print("Computer input: scissors")
            print("Computer wins!")
            computer_scores += 1
            
        elif computer_input == "paper":
            print("Your input: paper")
            print("Computer input: paper")
            print("It's a tie!")
            
            
    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input: scissors")
            print("Computer input: rock")
            print("Computer wins!")
            computer_scores += 1
            
        elif computer_input == "paper":
            print("Your input: scissors")
            print("Computer input: paper")
            print("You win!")
            user_scores += 1
            
        elif computer_input == "scissors":
            print("Your input: scissors")
            print("Computer input: scissors")
            print("It's a tie!")
            
    elif user_input != choices:
        print()
        print("Invalid input. Please, try again")
            
    


