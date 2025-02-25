#! /usr/bin/env python3

def translate_message(dictionary, message):
    translation = {}
    for entry in dictionary:
        english, foreign = entry.split()
        translation[foreign] = english
    
    translated_message = []
    for word in message:
        translated_message.append(translation.get(word, "eh"))
    
    return translated_message

if __name__ == "__main__":
    # Reading dictionary entries
    dictionary = []
    while True:
        entry = input().strip()
        if not entry:
            break
        dictionary.append(entry)
    
    # Reading the message
    message = []
    while True:
        try:
            word = input().strip()
            if not word:
                break
            message.append(word)
        except EOFError:
            break
    
    # Translating the message
    translated_message = translate_message(dictionary, message)
    
    # Output the translated message
    for word in translated_message:
        print(word)
