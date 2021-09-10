import random
import art
from game_data import data
import os
import time

clear = lambda: os.system('cls')

def choose_a_person():
    '''Chooses a random index from data and returns it's respective dictionary with it's person's information'''
    person = random.choice(data); return person

print(art.logo)

def game():
    '''Main function where the game is in fact located'''
    first_person = choose_a_person()
    second_person = choose_a_person()
    player_points = 0
    followers_reference = None

    guessing_right = True
    
    while guessing_right:
        print("Who do you think has more followers on Instagram?")
        print(f"Current points: {player_points}")
        print(f"A -> {first_person['name']}, {first_person['description']} from {first_person['country']}")
        print(art.versus)
        print(f"B -> {second_person['name']}, {second_person['description']} from {second_person['country']}")
        
        player_guess = input("Who has more followers? (A / B): ").lower()
        
        if player_guess == "a":
            player_guess = first_person['follower_count']
            followers_reference = second_person['follower_count']
        elif player_guess == "b":
            player_guess = second_person['follower_count']
            followers_reference = first_person['follower_count']
        else:
            print("You need to type 'A' or 'B'. Ending the game...")
            time.sleep(2)
            clear()
            return

        if player_guess > followers_reference:
            time.sleep(0.2)
            clear()
            player_points += 1
            first_person = second_person
            second_person = choose_a_person()
        elif player_guess < followers_reference:
            guessing_right = False
            print(f"Your acquired a total of {player_points} points!")
            print(art.game_over)
            print("Ending the game...")
            time.sleep(5)
            clear()
            
            play_again = input("Do you want to play again? (Y / N): ").lower()
            
            if play_again == "y":
                clear()
                game()
            else:
                clear()
                return
                
game()