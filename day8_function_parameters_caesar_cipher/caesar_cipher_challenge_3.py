from art.logo import logo

# Display logo first
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Implement the Caeser-Cipher (text encryption and decryption) 
def caesar_cipher(direction, text, shift):
    # applying shift and unshift position
    if direction == "decode":
        shift *= -1
        # on "encode" do nothing
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            # pushed into cipher text list
            new_position = position + shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter

    return print(f"\nYour {direction}d text is: {cipher_text}")

go_again = 'yes'
while go_again == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Call the cipher function
    caesar_cipher(direction, text, shift)

    go_again = input("Type 'yes' if you want to go again, otherwise type 'no': ").lower()
else:
    print("Good Bye!")