import base64
from Crypto.Hash import SHA256, MD5, SHA1
from AESCipher import AESCipher
from DESCipher import DESCipher
from ElgamalCipher import ElgamalCipher
from chatClientFinal import chat_client
import pyfiglet
import time

from getout import getout

# Nom.Prenom@insat.ucar.tn - Nom :6 chars - Prenom : 5 chars -> insat.dic
# etape 2 => insérer un email à hacher
# etape 3 => craquer le hash de cet email en s’appuyant sur insat.dic

# crunch 26 26 -t @@@@@@.@@@@@@insat.ucar.tn -l aaaaaaaaaaaa@aaaaaaaaaaaaa -o insat.dic
# crunch 17 17 -t @.@@insat.ucar.tn -l aaa@aaaaaaaaaaaaa -o insat.dic


def insertEmail(email):
    # Open a file with access mode 'a'
    file_object = open('insat.dic', 'a')
    # Append 'hello' at the end of file
    file_object.write("{}\n".format(email))
    # Close the file
    file_object.close()


def crack(obj, hashed):
    # Using readlines()
    file1 = open('insat.dic', 'r')
    for line in file1:
        if obj.new(line.replace("\n", "").encode()).hexdigest() == hashed:
            print("CRACKED IT! Your word is " + line)
            return
    print("Couldn't crack it...")



def menu(username):

    print("\n\t1- Encode or decode a message")
    print("\t2- Hash a message")
    print("\t3- Crack a hashed message")
    print("\t4- Symmetrical Crypt and decrypt of a message")
    print("\t5- ASymmetrical Crypt and decrypt of a message")
    print("\t6- Secure Communication between two clients")
    print("\t7- Exit")

    choix_1 = int(input("\n Your choice : "))

    if choix_1 == 1:
        print("\n\t1- Encode a message")
        print("\t2- Decode a message")

        choix_2 = int(input("\n Your choice : "))

        if choix_2 == 1:
            message = input("\nMessage :  ")
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print(base64_message)
        elif choix_2 == 2:
            base64_message = input("\nMessage :  ")
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            print(message)
        else:
            getout()

    elif choix_1 == 2:
        print("\n\t1- Md5")
        print("\t2- SHA1")
        print("\t3- SHA256")

        choix_2 = int(input("\n Your choice : "))

        if choix_2 == 1:
            str2hash = input("\nMessage :  ")
            result = MD5.new(data=str2hash.encode()).hexdigest()
            insertEmail(str2hash)
            print(result)
        elif choix_2 == 2:
            str2hash = input("\nMessage :  ")
            result = SHA1.new(data=str2hash.encode()).hexdigest()
            insertEmail(str2hash)
            print(result)
        elif choix_2 == 3:
            str2hash = input("\nMessage :  ")
            result = SHA256.new(data=str2hash.encode()).hexdigest()
            insertEmail(str2hash)
            print(result)
        else:
            getout()

    elif choix_1 == 3:
        print("\n\t1- Md5")
        print("\t2- SHA1")
        print("\t3- SHA256")

        choix_2 = int(input("\n Your choice : "))

        if choix_2 == 1:
            strhashed = input("\nMessage :  ")
            obj = MD5
            crack(obj, strhashed)
        elif choix_2 == 2:
            strhashed = input("\nMessage :  ")
            obj = SHA1
            crack(obj, strhashed)
        elif choix_2 == 3:
            strhashed = input("\nMessage :  ")
            obj = SHA256
            crack(obj, strhashed)
        else:
            getout()

    elif choix_1 == 4:
        print("\n\t1- DES")
        print("\t2- AES256")

        choix_2 = int(input("\n Your choice : "))

        if choix_2 == 1:
            message = input("\nMessage :  ")
            cipher = DESCipher()
            encrypted = cipher.encrypt(message)
            print("\nEncrypt :  ", encrypted.hex())
            print("\nDecrypt :  ", cipher.decrypt(encrypted).decode())

        elif choix_2 == 2:
            message = input("\nMessage :  ")
            cipher = AESCipher()
            encrypted = cipher.encrypt(message)
            print("\nEncrypt :  ", encrypted.hex())
            print("\nDecrypt :  ", cipher.decrypt(encrypted).decode())

        else:
            getout()

    elif choix_1 == 5:
        print("\n\t1- RSA")
        print("\t2- Elgamal")

        choix_2 = int(input("\n Your choice : "))

        if choix_2 == 1:
            import RSA
        elif choix_2 == 2:
            message = input("\nMessage :  ")
            nchars = len(message)
            raw = sum(ord(message[byte])<<8*(nchars-byte-1) for byte in range(nchars))
            cipher = ElgamalCipher(16)
            u,v = cipher.encrypt(raw)
            print("\nEncrypt :  ( " , u, " , ",v, " )" )
            decrypted = cipher.decrypt(u,v)
            plaintext = ''.join(chr((decrypted>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))
            print("\nDecrypt :  " , plaintext )
        else:
            getout()

    elif choix_1 == 6:
        
        print(pyfiglet.figlet_format("Welcome to the chat room"))
        time.sleep(2)
        chat_client(username)


    elif choix_1 == 7:
        exit()

    else:
        getout()
    menu(username)


if __name__ == '__main__':
    main()