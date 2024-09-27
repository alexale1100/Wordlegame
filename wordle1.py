import random
import datetime
from PyDictionary import PyDictionary 

# Define word lists for each category and day of the week
word_categories = { #the variable "word_categories" is defined with either fruits, animals, or colors. 
    0: {  # Monday #The day of the week is indexed and the word list for that day is found by linking the list to the index of that day.
        "fruits": ["apple", "grape", "lemon", "peach", "berry"],
        "animals": ["tiger", "whale", "horse", "eagle", "zebra"],
        "colors": ["green", "black", "white", "lilac", "amber"]
    },
    1: {  # Tuesday
        "fruits": ["melon", "mango", "pearl", "guava", "olive"],
        "animals": ["shark", "koala", "panda", "rhino", "snake"],
        "colors": ["cream", "olive", "pearl", "ivory", "coral"]
    },
    2: {  # Wednesday
        "fruits": ["plums", "prune", "apple", "guava", "dates"],
        "animals": ["otter", "llama", "camel", "hyena", "bison"],
        "colors": ["beige", "blond", "mauve", "pearl", "green"]
    },
    3: {  # Thursday
        "fruits": ["kiwis", "lyche", "prune", "limes", "pears"],
        "animals": ["goose", "panda", "robin", "gecko", "zebra"],
        "colors": ["amber", "olive", "ebony", "black", "cream"]
    },
    4: {  # Friday
        "fruits": ["kiwis", "mango", "plums", "melon", "cocoa"],
        "animals": ["otter", "moose", "shark", "panda", "whale"],
        "colors": ["ivory", "lilac", "brown", "black", "white"]
    },
    5: {  # Saturday
        "fruits": ["apple", "prune", "grape", "limes", "lemon"],
        "animals": ["sloth", "robin", "rhino", "koala", "bison"],
        "colors": ["coral", "cream", "green", "brown", "ivory"]
    },
    6: {  # Sunday
        "fruits": ["melon", "dates", "berry", "apple", "olive"],
        "animals": ["zebra", "camel", "panda", "shark", "whale"],
        "colors": ["mauve", "lilac", "beige", "white", "black"]
    }
}

def is_valid_word(guess): #this function allows the code to see whether the word the player inputs is an actual word 
    """Check if the guess is a valid 5-letter word using PyDictionary."""
    if len(guess) != 5:
        return False
    
    try:
        # Check if the word exists in the dictionary
        meaning = dictionary.meaning(guess)
        return meaning is not None  # If meaning exists, it's a valid word
    except:
        return False  # If there's any issue (e.g., no internet), treat as invalid

# Store the last week when the words were shuffled
last_shuffled_week = None

def shuffle_word_lists():
    """Shuffle the word lists at the beginning of a new week."""
    global last_shuffled_week
    current_week = datetime.datetime.now().isocalendar()[1]  # Get the current week number

    # If it's a new week or the first time running the game, shuffle the lists
    if last_shuffled_week != current_week:
        print(f"Shuffling word lists for week {current_week}...")
        for day_categories in word_categories.values():
            for word_list in day_categories.values():
                random.shuffle(word_list)
        last_shuffled_week = current_week

def get_word_list_for_today(): #this function chooses the word list depending on the day. The word list is linked the the index, which determines the day. 
    # Get the current day of the week (0 = Monday, 6 = Sunday)
    current_day = datetime.datetime.now().weekday()
    return word_categories[current_day]

def get_feedback(guess, word): #this function prints the feedback the player will get after they guess a word. For exammple, "GGYBY". 
    feedback = ['_'] * 5  # Placeholder for feedback
    for i in range(5):
        if guess[i] == word[i]:
            feedback[i] = 'G'  # Correct letter and position (Green)
        elif guess[i] in word:
            feedback[i] = 'Y'  # Correct letter but wrong position (Yellow)
        else:
            feedback[i] = 'B'  # Incorrect letter (Blank/Black)
    return ''.join(feedback)

def play_wordle(): 
    # Shuffle the word lists if it's a new week
    shuffle_word_lists()

    # Get today's word lists
    word_lists = get_word_list_for_today()
    
    # Show available categories to the player
    categories = list(word_lists.keys())
    print("Categories for today:", ', '.join(categories))

    # Ask player to pick a category
    while True: #this part of the function ensures that the category the player picked is a valid category and that there is a word list for that category. 
        category = input("Pick a category: ").lower()
        if category in word_lists:
            break
        print(f"Invalid category! Please choose from: {', '.join(categories)}")
    

    # Pick a random word from the chosen category
    word = random.choice(word_lists[category]) #this code chooses a random code from the the word list of that category. 
    attempts = 6  # 6 tries

    print(f"Welcome to Wordle! Guess the 5-letter word from the '{category}' category.")
    
    for attempt in range(attempts):
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").lower() #this calculates the amount of guesses the player has left/which try they are on. 

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        if is_valid_word(guess):
                break
        print("Invalid word! Please enter a valid 5-letter word.")

        feedback = get_feedback(guess, word) 
        print("Feedback:", feedback) #this loops the code back to the feedback code which prints the validity of the letters the player chose. For example: "GGYBB"

        if guess == word:
            print("Congratulations! You've guessed the word correctly!")
            break
    else:
        print(f"Sorry, you've used all your attempts. The word was '{word}'.")

# Run the game
play_wordle()
