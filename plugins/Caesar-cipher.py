AUTHOR = "Mackenzie Klupp"
APP_NAME = "Caesar Cipher example"

def run():
    word = "hello"
    shift_value = 3
    shifted_word = ""

    for letter in word:
        shifted_word += chr((ord(letter) - ord('a') + shift_value) % 26 + ord('a'))

    return f"{APP_NAME} says: Original word {word} shifted by {shift_value} is {shifted_word}"