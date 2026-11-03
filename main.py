import random

#Function to start the game
def play_game():
    options = ("rock", "paper", "scissors")
    run_game = True
    while run_game:
        user_choice = None
        # Keep asking until the player enters one of the valid options.
        while user_choice not in options:
            user_choice = input("Enter rock, paper, or scissors: ").lower()
        computer_choice = random.choice(options) 
        print(f"\nyour choice: {user_choice}")
        print(f"\ncomputer's choice: {computer_choice}")
        
        if user_choice == computer_choice:
            print("\nIt's a tie!")
        # These are the three combinations where the player beats the computer.
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("\nYou win!")
        else:
            print("\nComputer wins!")
            
        if not input("\nDo you want to play again? (yes/no): ").lower() == "yes":
            run_game = False 
            print("\nThanks for playing!")
            
            
play_game()