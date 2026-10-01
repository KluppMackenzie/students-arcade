AUTHOR = "Mackenzie Klupp"
APP_NAME = "Caesar Cipher example"

def run():
    def run(): 
        word = random.choice(["hello", "world", "python", "programming"]) 
        shifted_word = "" 
        shift_options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 
        shift_value = random.choice(shift_options) 
        for letter in word: 
            shifted_word += chr((ord(letter) - ord('a') + shift_value) % 26 + ord('a')) 
        return f"{APP_NAME} says: Original word {word} shifted by {shift_value} is {shifted_word}"