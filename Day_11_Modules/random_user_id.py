# writ a funtion which generates a six digit/character
import random
import string

def generate_random_user_id(number_of_character):
    # Define possible characters: digits and letters
    characters = string.ascii_letters + string.digits
    
    # Generate a random ID with 6 characters
    random_user_id = ''.join(random.choice(characters) for i in range(number_of_character))
    
    return random_user_id

# Example usage