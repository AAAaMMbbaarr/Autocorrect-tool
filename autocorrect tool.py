import nltk
from nltk.corpus import words
from nltk.metrics import edit_distance

# Download the words corpus if not already downloaded
nltk.download('words')

# Load the list of valid English words
word_list = set(words.words())
def autocorrect(word):
    if word in word_list:
        return word

    # Find the closest word by edit distance
    closest_word = min(word_list, key=lambda x: edit_distance(word, x))
    return closest_word

# Function to correct a sentence
def autocorrect_sentence(sentence):
    corrected_sentence = ' '.join([autocorrect(word) for word in sentence.split()])
    return corrected_sentence

# Test the autocorrect function
input_text = "Ths is an exmple of a sencence with erors."
corrected_text = autocorrect_sentence(input_text)
print("Original:", input_text)
print("Corrected:", corrected_text)
