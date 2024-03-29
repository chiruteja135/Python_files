import colorama
import os
import enchant
from textblob import TextBlob
from collections import Counter

colorama.init()

def header():
    print(colorama.Style.BRIGHT + colorama.Fore.BLUE + "*" * os.get_terminal_size().columns)
    print(" " * (os.get_terminal_size().columns // 2) + "ENTER YOUR TEXT BELOW")
    print("*" * os.get_terminal_size().columns)

def take_input():
    text = input(colorama.Fore.GREEN + '')
    return text

def operations_on_input(text):
    dictionary = enchant.Dict("en_US")  # Creating an object of the English dictionary
    corrected_text = []
    wrong_words = {}
    for word in text.split():  # Splitting the whole text into words
        if dictionary.check(word):
            corrected_text.append(word)
        else:
            suggestions = dictionary.suggest(word)
            if suggestions:
                corrected_word = suggestions[0]  # Use the first suggestion as the corrected word
                corrected_text.append(corrected_word)
                wrong_words[word] = corrected_word
            else:
                corrected_text.append(word)  # If no suggestions, keep the original word
    
    # Convert list of corrected words to a string
    corrected_text_str = ' '.join(corrected_text)
    
    # Perform grammar check using TextBlob
    corrected_grammar_text = TextBlob(corrected_text_str).correct()
    
    return corrected_text_str, wrong_words, corrected_grammar_text

def display_output(original_text, corrected_text, wrong_words, corrected_grammar_text, sentiment_polarity):
    print((colorama.Style.BRIGHT + colorama.Fore.BLUE + "*" * os.get_terminal_size().columns))
    print(colorama.Fore.YELLOW + "ORIGINAL TEXT ENTERED : ")
    print(colorama.Fore.CYAN + original_text)
    print(colorama.Fore.BLUE + "\nCORRECTED GRAMMAR TEXT : ")
    print(colorama.Fore.CYAN + str(corrected_grammar_text))
    print(colorama.Fore.MAGENTA + f"\nSENTIMENT POLARITY: {sentiment_polarity}")
    print(colorama.Fore.RED + "\nERRORS IDENTIFIED AND CORRECTED : ")
    for i, (wrong_word, corrected_word) in enumerate(wrong_words.items()):
        print(f"{i+1}. {wrong_word} -> {corrected_word}")
    print(colorama.Fore.YELLOW + "\nWORD FREQUENCY : ", end='')
    word_freq = Counter(corrected_text.split())
    for word, freq in word_freq.items():
        print(f"{word}: {freq}", end=' | ')

def run_spell_check():
    while True:
        header()
        original_text = take_input()
        corrected_text, wrong_words, corrected_grammar_text = operations_on_input(original_text)
        # Sentiment polarity without adjusting for grammar
        sentiment_polarity = TextBlob(original_text).sentiment.polarity
        display_output(original_text, corrected_text, wrong_words, corrected_grammar_text, sentiment_polarity)

        # Ask user if they want to exit or continue
        print("\n\nDo you want to continue (press 'y' for yes or any other key to exit)?")
        choice = input().strip().lower()
        if choice != 'y':
            break

run_spell_check()
