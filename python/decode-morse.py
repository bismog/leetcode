#!/usr/bin/env python

def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    splited_words = morseCode.split('   ')
    decoded_string = ''
    for word in splited_words:
        splited_characters = word.split(' ')
        for ch in splited_characters:
            decoded_string += MORSE_CODE[ch]
        decoded_string += ' '
    return decoded_string.strip()

MORSE_CODE = {
    "....": "H",
    ".": "E",
    "-.--": "Y",
    ".---": "J",
    "..-": "U",
    "-..": "D",
    "   ": " "
}

decoded = decodeMorse(".... . -.--   .--- ..- -.. .")
print '"' + decoded + '"'
#decoded = decodeMorse("             ")
#print '"' + decoded + '"'
