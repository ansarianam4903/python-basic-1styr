# 11. VOWELCHECKER

def is_vowel(char):
  vowels = "aeiouAEIOU"

  if len(char) == 1 and char in vowels:
    return True
  return False 

# Test
print(is_vowel('a'))
print(is_vowel('b'))



