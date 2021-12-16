"""Ciphers by Joseph Devincenzi dev15010@byui.edu
Ciphers are systems for encrypting and decrypting
data. A cipher converts an original message into 
a secret message by changing the order of the 
letters used"""

try: 
    import pyperclip #copies things to clipboard autmoatically
except ImportError:
    pass  #since it's not a critical part it's ok if not used.

print("Ciphers by Joseph Devincenzi")
print(
    """Ciphers have been used for thousands of years to send secret messages. 
Type the message you wish to encrypt and then choose the method
of encryption. This program offers three methods. 1 is a Caeser Cipher that you 
type a messge with a key. The key determines the number of shifts to change the 
letter. For instance is my key is 2, then A becomes C etc. Number 2 is a ROT13 
cipher. It simply is like a Caeser Cihper but the key is always 13. Finally, there
is a vingere cipher. Vingere ciphers up until the invention of major computing 
computers was the height of cryptography. Instead of entering a number to shift
the letter, one enters a key word that then determines the shift of the letters. 
For instance if my Key word is "CAT" C is a shift of 2, A is 0, and T is 19. So the 
first letter of the message is shifted by 2 the second letter by 0 and the third 
letter by 19. Then it repeats. You don't need to type an actual "word" but it could
be any combination of letters, creating a very complicated code to crack. 
"""
)

#symbols list for the caeserCipher, you could change these if you'd like
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    way = getMode()
    if way == "encrypt":
        print()
        print(
"""How would you like to encrypt your message?
1. Caeser Cipher 
   Enter a number key that will jumble the letters to your message

2. ROT13 Cipher
   No key number required automatically encrypted

3. Vingere Cipher
   Enter a key that is a word to jumble the letters
   
"""
)
        print("Insert a number")
        encryptMethodChoice = input("> ")
        if encryptMethodChoice == "1":
            caeserMessage = getMessageToEncrypt()
            caeserKey = getKey()
            caeserEncryptedMessage = caeserCipherEncrypt(caeserMessage, caeserKey)
            print(f"Your encrypted message is: {caeserEncryptedMessage}")
            try: 
                pyperclip.copy(caeserEncryptedMessage)
                print("Encrypted message copied to keyboard")
            except: 
                pass
        
        elif encryptMethodChoice == "2":
            rot13Message = getMessageToEncrypt()
            rot13EncryptyedMessage = caeserCipherEncrypt(rot13Message, 13)
            print(f"Your encrypted message is: {rot13EncryptyedMessage}")
            try: 
                pyperclip.copy(rot13EncryptyedMessage)
                print("Encrypted message copied to keyboard")
            except: 
                pass

        elif encryptMethodChoice == "3":
            vingereMessage = getMessageToEncrypt()
            vingereKey = getVigenereKey()
            vingereEncryptedMessage = vingereCipherEncrypt(vingereMessage, vingereKey)
            print(f"Your encrypted message is: {vingereEncryptedMessage}")
            try: 
                pyperclip.copy(vingereEncryptedMessage)
                print("Encrypted message copied to keyboard")
            except: 
                pass

    else: 
        print(
"""What kind of cipher was used to encrypt?
1. Caeser Cipher
2. ROT13 Cipher
3. Vingere Cipher"""
        )            
        print("Enter a number")
        decryptMethodChoice = input("> ")

        if decryptMethodChoice == "1":
            print("Do you (k)now the key or would you like to (b)rute-force?")
            caeserDecryptMode = input("> ").lower()
            if caeserDecryptMode.startswith("k"):
                decryptKey = getDecryptKey()
                caeserMessageDecrypt = getMessageToDecrypt()
                caeserDecryptedMessage = caeserCipherDecrypt(caeserMessageDecrypt, decryptKey)
                print(f"Your decrypted message is: {caeserDecryptedMessage}")
                try: 
                    pyperclip.copy(caeserDecryptedMessage)
                    print("Decrypted message copied to keyboard")
                except: 
                    pass
            elif caeserDecryptMode.startswith("b"):
                caeserMessageDecrypt = getMessageToDecrypt()
                caeserHacker(caeserMessageDecrypt)

        elif decryptMethodChoice == "2":
            rot13MessageDecrypt = getMessageToDecrypt()
            rot13DecryptedMessage = caeserCipherDecrypt(rot13MessageDecrypt, 13)
            print(f"Your decrypted message is: {rot13DecryptedMessage}")  
            try: 
                pyperclip.copy(rot13DecryptedMessage)
                print("Decrypted message copied to keyboard")
            except: 
                pass          
        
        elif decryptMethodChoice == "3":
            vingereMessageDecrypt = getMessageToDecrypt()
            vingereKey = getVigenereKey()
            vingereDecryptedMessage = vingereCipherDecrypt(vingereMessageDecrypt, vingereKey)
            print(f"Your decrypted message is: {vingereDecryptedMessage}")
            try: 
                pyperclip.copy(vingereDecryptedMessage)
                print("Decrypted message copied to keyboard")
            except: 
                pass 

#finds out from user if we are encrypting or decrypting a message
def getMode():
    while True:
        print("Do you want to (e)ncrypt or (d)ecrpyt a message?")
        answer = input("> ").lower()
        if answer.startswith("e"):
            way = "encrypt"
            break
        elif answer.startswith("d"):
            way = "decrypt"
            break
        print("Please enter e or d")
    return way

#gets the message from the user to encrypt
def getMessageToEncrypt():
    print("Enter the message to encrypt.")
    message = input("> ")
    return message

def getMessageToDecrypt():
    print("Enter the message to decrypt.")
    message = input("> ")
    return message

def getKey():
    #gets a user key for the Caeser Cipher 
    while True: #keeps asking till a correct key is entered
        maxKey = len(SYMBOLS) - 1
        print(f"Please enter the key (0 to {maxKey}) to use")
        response = input("> ").upper()

        if not response.isdecimal():
            continue
        
        if 0 <= int(response) < len(SYMBOLS):
            key = int(response)
            break
    return key

def getDecryptKey():
    while True: #keeps asking till a correct key is entered
        print(f"Please enter the key used to encrypt the message: ")
        response = input("> ").upper()

        if not response.isdecimal():
            continue
        
        if 0 <= int(response) < len(SYMBOLS):
            key = int(response)
            break
    return key


def getVigenereKey():
    while True:
        print("Please specify the key to use.")
        print("It can be a word or any combination of letters.")
        answer = input("> ").upper()
        if answer.isalpha():
            key = answer
        return key



def caeserCipherEncrypt(message, key):
    #works only with uppercase letters since our symbols are defined as such.
    message = message.upper()
    encryptedMessage = ""
    #encrypts the message
    for s in message:
        if s in SYMBOLS:
            number = SYMBOLS.find(s)
            number = number + key

            if number >= len(SYMBOLS):
                number = number - len(SYMBOLS)
            elif number < 0:
                number = number + len(SYMBOLS)
        
            encryptedMessage = encryptedMessage + SYMBOLS[number]
        else:
            encryptedMessage = encryptedMessage + s
    
    return encryptedMessage

def caeserCipherDecrypt(message, key):
    message = message.upper()
    encryptedMessage = ""
    #decrypts the message
    for s in message:
        if s in SYMBOLS:
            number = SYMBOLS.find(s)
            number = number - key

            if number >= len(SYMBOLS):
                number = number - len(SYMBOLS)
            elif number < 0:
                number = number + len(SYMBOLS)
        
            encryptedMessage = encryptedMessage + SYMBOLS[number]
        else:
            encryptedMessage = encryptedMessage + s
    
    return encryptedMessage

def caeserHacker(message):
    message = message.upper()
    for i in range(len(SYMBOLS)):
        translated = ''
        for s in message:
            if s in SYMBOLS:
                number = SYMBOLS.find(s)
                number = number - i

                if number < 0: 
                    number = number + len(SYMBOLS)

                translated = translated + SYMBOLS[number]
            else: 
                translated = translated + s
        print("Key #{}: {}".format(i, translated))

def vingereCipherEncrypt(message, key):
    encryptedMessage = []

    keyIndex = 0
    key = key.upper()

    for s in message:
        number = SYMBOLS.find(s.upper())
        
        if number != -1: #checks to make sure 
            number += SYMBOLS.find(key[keyIndex])
            number %= len(SYMBOLS) #handles if there is a wrap aound with the message
            
            if s.isupper():
                encryptedMessage.append(SYMBOLS[number])
            elif s.islower():
                encryptedMessage.append(SYMBOLS[number].lower())
            
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        
        else:
            encryptedMessage.append(s)

    return ''.join(encryptedMessage)

def vingereCipherDecrypt(message, key):
    encryptedMessage = []

    keyIndex = 0
    key = key.upper()

    for s in message:
        number = SYMBOLS.find(s.upper())
        
        if number != -1: #checks to make sure 
            number -= SYMBOLS.find(key[keyIndex])
            number %= len(SYMBOLS) #handles if there is a wrap aound with the message
            
            if s.isupper():
                encryptedMessage.append(SYMBOLS[number])
            elif s.islower():
                encryptedMessage.append(SYMBOLS[number].lower())
            
            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        
        else:
            encryptedMessage.append(s)

    return ''.join(encryptedMessage)


if __name__ == "__main__":
    main()








