# create alphabet dictionary with a right shift of 5
encrypted_keys = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a", 
    "w": "b",
    "x": "c",
    "y": "d", 
    "z": "e",
}

# creating a welcome message
welcome_msg = "Welcome to the Caesar Cipher!"
print(welcome_msg)

# creating the input for user sentence that will be encrypted below
user_sentence = input("Please enter a sentence here: ")
user_sentence = user_sentence.lower()

# creating the encrypted message from the user sentence above
secret_message = ""
for char in user_sentence:
        if char in encrypted_keys:
            char = encrypted_keys[char]
        secret_message += char
print("Your secret message is displayed here: ", secret_message)

# creating a goodbye message
goodbye_msg = "See you next time."
print(goodbye_msg)







