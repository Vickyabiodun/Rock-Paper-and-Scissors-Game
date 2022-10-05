"""Import the random module"""
"""The try and except improves the app feedback so if anything goes wrong, there is an organized feedback inputed by creator"""
try:
    import random

    """Images are ascii art and are avaialble online"""
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''

    """Create a list from the three variables above"""
    game_images = [rock, paper, scissors]

    """Ask for user input since it's a game between a user and the computer"""
    user_choice = int(input('please press 0 for rock, 1 for scissor and 2 for paper. \n'))

    """Conditional statement to ensure users can only pick numbers between 0 and 2"""
    if user_choice>=3 or user_choice < 0 :
        print('inavlid selction, you lose')
    else:
        print(f'you chose {game_images[user_choice]}')
        """The comp_choice is a randomly generated number which makes the computer choice not predictable"""
        comp_choice = random.randint(0,2)
        print(f' The computer chose {comp_choice} {game_images[comp_choice]}')
        """Conditional statement stating who wins per time"""
        if user_choice == 0 and comp_choice == 2:
            print('you win')
        elif user_choice == 2 and comp_choice == 0:
            print('you lose')
        elif user_choice > comp_choice:
            print("You win!")
        elif user_choice < comp_choice:
            print("You lost!")
        elif comp_choice == user_choice:
            print("It's a draw")
except:
    print('Please try again later')


