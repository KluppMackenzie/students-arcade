# Caesar Shift Plugin
# Shift value: 3
from random import random


AUTHOR = "Mackenzie Klupp"
APP_NAME = "Caesar Cipher example"

def run():
    word = "hello"
    shifted_word = ""
    responses = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    shift_value = random.choice(responses)
    for letter in word:
        shifted_word += chr((ord(letter) - ord('a') + shift_value) % 26 + ord('a'))

    return f"{APP_NAME} says: Original word {word} shifted by {shift_value} is {shifted_word}"