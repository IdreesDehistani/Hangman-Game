import random 
from words import words 
import string 

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word: 
        word = random.choice(words)
    return word.upper()

def get_hint(word_letters, used_letters, lives):
    remaining_letters = word_letters - used_letters
    if len(remaining_letters) > 0:
        if lives > 1 or len(remaining_letters) <= 2:
            return random.choice(list(remaining_letters))
        elif lives == 1: 
            # provide a hint of the first letter in the remaining letters
            return list(remaining_letters)[0]
    return None

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 
    lives = 8
    
    while len(word_letters) > 0 and lives > 0: 
        print(f'You have {lives} lives left and You have already guessed these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ''.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word.')
        
        elif user_letter in used_letters:
            print('You have already used that character, please try again.')
        else:
            print('Invalid character, please try again.')

        hint = get_hint(word_letters, used_letters, lives)  # Added missing parameter
        if hint:
            print(f'Hint: the word contains the letter {hint}')
            
        print() # add an empty line for readability
        
    if lives == 0:
        print(f'You died, sorry. The word was {word}!!')
    else:
        print(f'Congratulations, you guessed the word {word}!!')
        
hangman()
