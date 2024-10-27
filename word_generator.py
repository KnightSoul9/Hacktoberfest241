import random
import string

# Common English prefixes and suffixes
prefixes = ["pre", "un", "re", "in", "dis", "non", "over", "mis", "sub"]
suffixes = ["ing", "ed", "er", "ly", "tion", "s", "es", "ness", "ment"]

# Function to generate random word with complexity
def generate_complex_word(min_length=3, max_length=8, start_letter=None):
    # Randomize word length
    word_length = random.randint(min_length, max_length)
    
    # Initialize word with start letter if provided
    if start_letter:
        word = start_letter
        word_length -= len(start_letter)
    else:
        word = ""
    
    # Alternate consonants and vowels for more realistic sound patterns
    vowels = "aeiou"
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    
    for i in range(word_length):
        if i % 2 == 0:
            word += random.choice(consonants)  # Add consonant
        else:
            word += random.choice(vowels)      # Add vowel
    
    # Optionally add a prefix or suffix
    if random.random() < 0.5:
        word = random.choice(prefixes) + word
    if random.random() < 0.5:
        word += random.choice(suffixes)
    
    return word

# Generate a list of complex words
def generate_complex_words(num_words=10, min_length=3, max_length=8, start_letter=None):
    return [generate_complex_word(min_length, max_length, start_letter) for _ in range(num_words)]

# Example usage
complex_words = generate_complex_words(num_words=10, min_length=4, max_length=10, start_letter="b")
print("Generated complex words:", complex_words)
