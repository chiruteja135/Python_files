import colorama
import os
import enchant
from textblob import TextBlob
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize
import googletrans
import time

colorama.init()
nltk.download('stopwords')

def header():
    print(colorama.Style.BRIGHT + colorama.Fore.BLUE + "*" * os.get_terminal_size().columns)
    print(colorama.Fore.YELLOW + " " * (os.get_terminal_size().columns // 2) + "ENTER YOUR TEXT BELOW")
    print(colorama.Style.BRIGHT + colorama.Fore.BLUE + "*" * os.get_terminal_size().columns)

def take_input():
    text = input(colorama.Fore.GREEN + '')
    return text

def operations_on_input(text):
    dictionary = enchant.Dict("en_US") 
    corrected_text = []
    wrong_words = {}
    for word in text.split():
        if dictionary.check(word):
            corrected_text.append(word)
        else:
            suggestions = dictionary.suggest(word)
            if suggestions:
                corrected_word = suggestions[0]
                corrected_text.append(corrected_word)
                wrong_words[word] = corrected_word
            else:
                corrected_text.append(word)

    # CONVERTING THE LIST TO STRING
    corrected_text_str = ' '.join(corrected_text)

    # GRAMMAR CHECK
    corrected_grammar_text = TextBlob(corrected_text_str).correct()

    # TRANSLATION
    try:
        # Perform language translation
        translator = googletrans.Translator()  # Use default service urls for automatic selection
        translated_text = translator.translate(corrected_text_str, dest='fr')  # Translate to French
    except Exception as e:
        print(f"Translation failed: {e}")
        translated_text = None

    # SUMMERIZATION
    sentences = sent_tokenize(corrected_text_str)
    summarized_text = ' '.join(sentences[:2])  # Summarize the first two sentences
    
    # SENTIMENT POLARITY
    sentiment_polarity = TextBlob(corrected_text_str).sentiment.polarity

    return corrected_text_str, wrong_words, translated_text, summarized_text, corrected_grammar_text, sentiment_polarity

def display_output(original_text, corrected_text, wrong_words, translated_text, summarized_text, corrected_grammar_text, sentiment_polarity):
    print((colorama.Style.BRIGHT + colorama.Fore.BLUE + "*" * os.get_terminal_size().columns))

    # ORIGINAL TEXT WILL BE DISPLAYED HERE
    print(colorama.Fore.YELLOW + "ORIGINAL TEXT ENTERED : ")
    print(colorama.Fore.CYAN + original_text)

    #CORRECTED TEXT WILL BE DISPLAYED  HERE
    print(colorama.Style.BRIGHT + colorama.Fore.BLUE + "\nCORRECTED GRAMMAR TEXT : ")
    print(colorama.Fore.GREEN + str(corrected_grammar_text))

    #ERRORRS IDENTIFIED WILL BE DISPLAYED HERE
    print(colorama.Fore.RED + "\nERRORS IDENTIFIED AND CORRECTED : ")
    for i, (wrong_word, corrected_word) in enumerate(wrong_words.items()):
        print(f"{i+1}. {colorama.Fore.RED + wrong_word} -> {colorama.Fore.GREEN + corrected_word}")

    #TRANSLATED AND SUMMARIZED TEXT WILL BE DISPLAYED HERE
    print(colorama.Style.BRIGHT + colorama.Fore.BLUE + "\nTRANSLATED TEXT : ")
    if translated_text:
        print(colorama.Fore.YELLOW + str(translated_text.text))
    else:
        print(colorama.Fore.YELLOW + "Translation failed.")
    
    #SUMMARIZED TEXT WILL BE DISPLAYED HERE
    print(colorama.Style.BRIGHT + colorama.Fore.BLUE + "\nSUMMARIZED TEXT : ")
    print(colorama.Fore.YELLOW + summarized_text)

    # SENTIMENT POLARITY WILL BE DISPLAYED HERE
    print(colorama.Style.BRIGHT + colorama.Fore.BLUE + "\nSENTIMENT POLARITY: ")
    print(colorama.Fore.YELLOW + str(sentiment_polarity))

    # WORD FREQUENCY WILL BE DISPLAYED HERE
    word_freq = Counter(corrected_text.split())
    print(colorama.Fore.RED + "\nWORD FREQUENCY : ", end='')
    for word, freq in word_freq.items():
        print(f"{word}: {freq}", end=' | ')

def run_spell_check():
    #Header
    header()
    #Input
    original_text = take_input()
    start_time=time.time()
    #Process
    corrected_text, wrong_words, translated_text, summarized_text, corrected_grammar_text, sentiment_polarity = operations_on_input(original_text)
    #output
    display_output(original_text, corrected_text, wrong_words, translated_text, summarized_text, corrected_grammar_text, sentiment_polarity)
    end_time=time.time()
    response_time=(end_time-start_time)
    # response time
    print(colorama.Style.BRIGHT + colorama.Fore.BLUE + "\nRESPONSE TIME : ")
    print(colorama.Fore.GREEN + str(response_time))


run_spell_check()
