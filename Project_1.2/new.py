import random

# Function to determine the outcome of the game
def gamewin(comp, you):
    if comp == you:
        return None  # Tie
    if (comp == 's' and you =='k') or \
    (comp == 'p' and you== 's') or\
    (comp == 'k' and you == 'p'):
        return False
    
    if (comp == 'k' and you =='s') or \
    (comp == 's' and you== 'p') or\
    (comp == 'p' and you == 'k'):
        return True

# Randomly choose a move for the computer
comp = random.choice(['s', 'p', 'k'])

# Get user's choice
you = input("Choose Stone(s) Paper(p) Scissor(k): ").lower()

# Ensure user input is valid
if you not in ['s', 'p', 'k']:
    print("Invalid input! Please choose 's', 'p', or 'k'.")
else:
    # Determine the winner
    result = gamewin(comp, you)
    
    # Display choices and result
    print(f"The computer chose {comp}.")
    print(f"You chose {you}.")
    
    if result is None:
        print("It's a tie!")
    elif result:
        print("You win!")
    else:
        print("You lose!")
