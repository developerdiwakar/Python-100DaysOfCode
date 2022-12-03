alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Implement the Caeser-Cipher (text encryption and decryption) 
def caesar_cipher(direction, text, shift):
    cipher_text = []
    # applying shift and unshift position
    if direction == "decode":
        shift *= -1

    for i in range(len(text)):
        letter = text[i]
        position = alphabet.index(letter)
        shift_unshift = alphabet[position + shift]
        # pushed into cipher text list
        cipher_text.insert(i, shift_unshift) 

    return print(f"\nYour {direction}d text is: {''.join(cipher_text)}")

# Call the cipher function
caesar_cipher(direction, text, shift)