alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# print(alphabet[7-26+5]) # h => m
# print(alphabet[4-26+5]) # e => j
# print(alphabet[11-26+5]) # l => q
# print(alphabet[11-26+5]) # l => q
# print(alphabet[14-26+5]) # o => t
# exit()
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    
def encrypt(text, shift):
    encrypted_text = []
    for i in range(len(text)):
        letter = text[i]
        position = alphabet.index(letter)
        
        # shifting letter
        shifted_letter = alphabet[position - 26 + shift]
        encrypted_text.insert(i, shifted_letter) 

    return "".join(encrypted_text)
    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

def decrypt(encrypted_text, shift_back):
    decrypted_text = []
    for i in range(len(encrypted_text)):
        letter = encrypted_text[i]
        position = alphabet.index(letter)
        
        # shifting letter back
        shifted_letter = alphabet[position - 26 - shift_back]
        decrypted_text.insert(i, shifted_letter) 
    
    return "".join(decrypted_text)


if direction == "encode":
    print(encrypt(text, shift))
else:
    print(decrypt(text, shift))