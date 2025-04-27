alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



def encrypt(original_text, num_of_shift):
    cipher_text = ''

    for letter in original_text:
        new_position = alphabet.index(letter) + num_of_shift
        cipher_text += alphabet[new_position]

    print(f'Your encrypted word is: \n{cipher_text}')


def decrypt(cipher_text, num_of_shift):
    original_text = ''

    for letter in cipher_text:
        new_position = alphabet.index(letter) - num_of_shift
        original_text += alphabet[new_position]

    print(f'Your decrypted word is: \n{original_text}')

    
#encrypt(text, shift)
while True:
    type = input("Encrypt/Decrypt? (e/d) \n").lower()
    if type == "e" or type == "d":
        break
    else:
        print("Invalid. Please enter 'e' or 'd'.\n")


text = input("Enter the text:\n").lower()
shift = int(input("Type of encryption/decryption (1-10):\n"))

if type == "e":
    encrypt(text,shift)
elif type == "d":
    decrypt(text, shift)
    

# decrypt function