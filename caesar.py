import argparse

alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
            'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

def cipher(text,k):
    #Mod of the sum of the index of the letter used and k.
    new_text = ""
    key_list = list(alphabet.keys())
    val_list = list(alphabet.values())

    for char in text:
        #Check if its a letter
        if char.isalpha():
            #Handling Upper case and lower case
            if (char.isupper()):
                position = val_list.index((alphabet[char.lower()]+k)%26)
                new_text += key_list[position].upper()
            else:
                position = val_list.index((alphabet[char]+k)%26)
                new_text += key_list[position]
        else:
            new_text += char
    return new_text


if __name__ == '__main__':
    #Creation of docs for python Script
    parser = argparse.ArgumentParser(description='Cipher Text trought Caesar Cipher.')
    parser.add_argument("k", type=int)
    args = parser.parse_args()
    plaintext = str(input("plaintext: "))
    ciphertext = cipher(plaintext,args.k)
    print ("ciphertext:",ciphertext)


