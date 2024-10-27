alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Don't change the code above
# TODO -1 Create a function called 'encrypt' that takes the 'text and 
# shift as inputs. 

def encrypt(plain_text,plain_shift):
    cipher_text=" "
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + plain_shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"{cipher_text}")
    # return cipher_text

    # TODO-2  Inside the 'encrypt' function, shift each letter of the 
    # 'text' forwards in the alphabet by the shift amount and print the encrypted text. 

    # #e.g
    # plain_text = 'hellow'
    # shift =5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

# TODO-3 Call the encrypt function and pass in the user inputs. You should
# be able to test the code and encrypt the message.

#TODO-1: Create a different function called 'decrypt' that takes the 
# 'text' and 'shift' as inputs.

def decrypt(plain_text,plain_shift):
    decrypt_text=" "
    for letter in plain_text:
        position1 = alphabet.index(letter)
        new_position = position1 - plain_shift
        decrypt_text += alphabet[new_position]
    print(f"{decrypt_text}")


#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text'
#  *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by 
# checking the 'direction' variable. Then call the correct function based 
# on that 'drection' variable. You should be able to test the code to
#  encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(plain_text=text,plain_shift=shift)
elif direction == "decode":
    decrypt(plain_text=text,plain_shift=shift)
