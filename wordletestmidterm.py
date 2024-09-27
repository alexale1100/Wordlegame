import unittest #this is a test for the code that checks the validity of the 5 letter word chosen by the player. It does not test the whole set of code for the game. 
from PyDictionary import PyDictionary

# Initialize PyDictionary
dictionary = PyDictionary()

# Function to check if the word is a valid 5-letter word using PyDictionary
def is_valid_word(guess):
    """Check if the guess is a valid 5-letter word using PyDictionary."""
    if len(guess) != 5:
        return False
    
    try:
        # Check if the word exists in the dictionary using PyDictionary 
        meaning = dictionary.meaning(guess) 
        return meaning is not None  # If meaning exists then the word is valid 
    except:
        return False  

# Test cases for is_valid_word function
class TestIsValidWord(unittest.TestCase):

    def test_valid_word(self):
        # the code tests a valid word, in this case it is "apple", a 5 letter word in the fruit category 
        self.assertTrue(is_valid_word("apple"), "'apple' should be a valid word")

    def test_invalid_word_length(self):
        # the code tests an invalid word: "dog" is not 5 letters
        self.assertFalse(is_valid_word("dog"), "'dog' is not 5 letters, should return False")

    def test_non_existent_word(self):
        # the code tests a 5-letter non-existent word that is invalid
        self.assertFalse(is_valid_word("zzzzz"), "'zzzzz' is not a valid word, should return False")

    def test_valid_but_longer_word(self):
        # the code tests a valid word but with more than 5 letters
        self.assertFalse(is_valid_word("banana"), "'banana' is longer than 5 letters, should return False")

    def test_valid_but_shorter_word(self):
        # the code tests a valid word but with fewer than 5 letters
        self.assertFalse(is_valid_word("cat"), "'cat' is shorter than 5 letters, should return False")

    def test_special_characters(self):
        # the code test a word with special characters, which should return as false as it is not a valid word.
        self.assertFalse(is_valid_word("appl$"), "'appl$' contains a special character, should return False")

    def test_uppercase_word(self):
        # the code test a valid word in uppercase, which should return as valid
        self.assertTrue(is_valid_word("APPLE"), "'APPLE' should be valid, case insensitive")

    def test_mixed_case_word(self):
        # the code tests a word with mix-letters of uppercase and lower case, and should return as valid since the word is valid 
        self.assertTrue(is_valid_word("ApPlE"), "'ApPlE' should be valid, case insensitive")

if __name__ == '__main__':
    unittest.main()
