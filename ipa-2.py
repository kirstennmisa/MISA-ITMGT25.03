#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Shift Letter

def shift_letter(letter, shift):
    
    if str(letter) == " ":
        return " "
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.index(str(letter))
    # Looks for the letter's position in the alphabet
    shifted_index = (index + int(shift)) % len(alphabet)
    # Gets remainder to wrap the letter around
    shifted_letter = alphabet[shifted_index]
    
       
    return shifted_letter


# In[2]:


# Caesar Cipher

def shift_letter(letter, shift):

    if str(letter) == " ":
        return " "
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.index(letter)
    # Looks for the letter's position in the alphabet
    shifted_index = (index + int(shift)) % len(alphabet)
    # Gets remainder to wrap the letter around
    shifted_letter = alphabet[shifted_index]
           
    return shifted_letter

def caesar_cipher(message, shift):
    
    shifted_message = ""
    # Empty to contain shifted message later
    
    for letter in message:
        shifted_letter = shift_letter(letter, shift)
        # Shifts each letter
        shifted_message += shifted_letter
        # Concatenates shifted letters
    
    return shifted_message


# In[3]:


# Shift By Letter

def shift_by_letter(letter, letter_shift):
    
    if str(letter) == " ":
        return " "
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_shift_value = alphabet.index(letter_shift)
    # Looks for the number equivalent of letter    
    index = alphabet.index(letter)
    # Looks for the letter's position in the alphabet
    shifted_index = (index + int(letter_shift_value)) % len(alphabet)
    # Gets remainder to wrap the letter around
    shifted_letter = alphabet[shifted_index]

    return shifted_letter


# In[4]:


# Vigenere Cipher

def vigenere_cipher(message, key):
    
    # Extend the key to match the length of the message
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]

    encrypted_message = ""
    for i, char in enumerate(message):
        if char == " ":
            encrypted_message += " "
        else:
            char_shift = ord(key[i]) - ord("A")
            encrypted_char = chr((ord(char) - ord("A") + char_shift) % 26 + ord("A"))
            encrypted_message += encrypted_char

    return encrypted_message


# In[5]:


# Scytale Cipher

def scytale_cipher(message, shift):
    
    if len(message) % shift != 0:
        message += "_" * (shift - len(message) % shift)
    # Checks if length of message is multiple of shift
    # Adds underscores if otherwise

    encoded_message = ""
    for i in range(len(message)):
        index = (i // shift) + (len(message) // shift) * (i % shift)
        encoded_message += message[index]
    # Calculates index of character in encoded message

    return encoded_message


# In[6]:


# Scytale Decipher

def scytale_decipher(message, shift):
    
    num_columns = len(message) // shift
    num_rows = shift
    # Calculates number of columns and rows in grid

    decoded_message = ""
    for row in range(num_rows):
        for col in range(num_columns):
            index = col * num_rows + row
            decoded_message += message[index]
    # Calculates index in original message based on row and column

    decoded_message = decoded_message.rstrip("_")
    # Removes underscores

    return decoded_message

