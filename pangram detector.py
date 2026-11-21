
# 15. Pangram Detector
# A pangram is a sentence that contains all 26 letters
# of the English alphabet at least once.

import string

def is_pangram(sentence):
    # Get all lowercase letters (a to z)
    alphabet = set(string.ascii_lowercase)

    # Convert sentence into lowercase and check
    # whether all alphabet letters are present
    return alphabet <= set(sentence.lower())


# Test
# First sentence does not contain all 26 letters
print(is_pangram("Hello World"))  # False

# Second sentence contains all 26 letters
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
