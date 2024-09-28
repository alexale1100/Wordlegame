# Wordlegame
Wordle Game Code: Siwei and Alexa

1. How long (cummulative) did you spend on the code?
   Cummulatively, the time our team spent on the code was approtximately 3-4 hours. We first tried to write our own functions. Then we used to code generated by ChatGPT to see where our code had errors and bugs. The main struggle at first was to write a function that would randomize and shuffle the word list. Similarly, we also struggled to write a function that would check the validity of the word by drawing from PyDictionary. 

2. What was the most time consuming part?
   The most time-consuming part of coding for WORDLE was checking over the word lists to ensure all the words were valid 5-letter words. Originally, ChatGPT generated some invalid words. For example, a long word would be cut down to 5 letters: "banana" is cut down to "banan". Thus, checking and changing the invalid words was extremely time consuming. While the process was not directly related to coding, it was time consuming. Secondly, the code for checking the validity of the word was written separately from the overall code so combining the two codes was also quite time consuming.

3. In retrosepct, how could you have worked more efficiently?
   Both my partner and I were working indivudally before combining our code since we were unsure of how to pull and push the same code file on github. Thus, the process was a little more time-consuming in inefficient.
   Secondly, based on our understanding, maybe we could have broken play_wordle() into smaller functions. For example: 
      initialize_game()pick_category()get_user_guess()display_feedback()

At the very beginning, we also spent quite a long time reading and trying to understand the code generated by chatgpt instead of putting our own logic into the code.

4. What libraries/starter code were most useful? To what extent did you need to modify them?
   We used ChatGPT and modified our code to fix any bugs or errors. The code is simple but we needed to modify the word lists as some words ChatGPT generated were not real valid words. Thus, we believe that the code generated by ChatGPT are quite prone to small errors that requires manual fixing. We also modified the code so that it would check whether the player's input word is a valid word using PyDictionary.
   
   We also used two of the very basic libraries in python, the Random used to shuffle the word lists and select random words for the game.

   Datetime was used to get the current date, day, and week number to manage word shuffling and category selection.

The starter code includes several basic functions including:

word_categories Dictionary:
This is a dictionary that maps each day of the week to a set of three word categories (fruits, animals, colors).
Each day (indexed from 0 to 6) has a list of words in each category.

last_shuffled_week # this is a variable:
This variable is used to track when the word lists were last shuffled, based on the current week number.

last_shuffled_week = None 
ensures the lists are shuffled the first time the game is played.

shuffle_word_lists() #this is a function:
This function checks if it’s a new week and, if so, shuffles all the word lists for each day and category. It updates last_shuffled_week to prevent reshuffling within the same week.

get_word_list_for_today() #this is a function:
This function retrieves the word lists for the current day of the week using datetime.datetime.now().weekday() (0 = Monday, 6 = Sunday).

We modify them from the very beginning, we establish the rule of the keeping track systems and chatGPT is just helping generating these functions and dictionaries.
