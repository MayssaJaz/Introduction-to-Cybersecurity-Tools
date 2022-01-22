import math
import pyfiglet
from tools import prime_check, pgcd, verify_primary_numbers, calculate_d

listOfSymbols = ['0', '1', '2', '3', '4', '5',
                 '6', '7', '8', '9', ' ', '!', '.', '?', '#']

print(pyfiglet.figlet_format("RSA Encryption / Decryption"))
 
def enter_pq():
    print("First we need two prime numbers p and q:")
    p = int(input("Value of p: "))
    q = int(input("Value of q: "))
    print("Checking your prime numbers...")
    check_p = prime_check(p)
    check_q = prime_check(q)
    while(((check_p == False) or (check_q == False))):
        print("You did not enter two prime numbers... Retry")
        p = int(input("Value of p: "))
        q = int(input("Value of q: "))
        check_p = prime_check(p)
        check_q = prime_check(q)
    print("You succefully entered two prime numbers!")

    n = p * q
    print("n = ", n)
    '''CALCULATION OF 'phi'.'''
    phi = (p-1)*(q-1)
    print("phi =", phi)
    print("============================")
    return(n,phi)


def calcule_e():
    test=enter_pq()
    n=test[0]
    phi=test[1]
    '''CALCULATION OF 'e'.'''
    for i in range(1, 1000):
        if(verify_primary_numbers(i, phi) == 1):
            e = i
    print("e =", e)
    public = (e, n)
    print("Public Key =", public)
    print("============================")
    return (n,phi,e)

def calcule_d():
    result=calcule_e()
    n=result[0]
    phi=result[1]
    e=result[2]
    '''CALCULATION OF 'd'.'''
    print("EUCLID'S ALGORITHM:")
    pgcd(e, phi)
    print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
    print("============================")
    print("EUCLID'S EXTENDED ALGORITHM:")
    d = calculate_d(e, phi)
    print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
    print("d=", d)
    print("============================")
    #public = (e, n)
    private = (d, n)
    print("Private Key =", private)
    #print("Public Key =", public)
    #print("============================")
    return(d,n,e)

# Encryption
'''ENCRYPTION ALGORITHM.'''


def encrypt(pub_key, n_text):
    test = False
    e, n = pub_key
    x = []
    m = 0
    for i in n_text:
        test = False
        for symbol in listOfSymbols:
            if (i == symbol):
                test = True
        if(test):
            x.append(400+listOfSymbols.index(i))
        else:
            if(i.isupper()):
                m = ord(i)-65
                c = (m**e) % n
                x.append(c)
            elif(i.islower()):
                m = ord(i)-97
                c = (m**e) % n
                x.append(c+27)
    return x


# Decryption
'''DECRYPTION ALGORITHM'''


def decrypt(priv_key, c_text):
    d, n = priv_key
    txt = c_text.split(',')
    x = ''
    m = 0
    for i in txt:
        if(int(i) >= 400):
            x += listOfSymbols[(int(i)-400)]
        else:
            if (int(i) >= 27):
                m = ((int(i)-27)**d) % n
                m += 97
                c = chr(m)
                x += c
            else:
                m = (int(i)**d) % n
                m += 65
                c = chr(m)
                x += c
    return x

"""
message = input(
    "Enter  the message you want to encrypt / decrypt?(PS: You will have to separate numbers with ',' for decryption):")
print("Your message is:", message)

choose = input("Choose your option :'1' => encryption / '2' => decrytion.")
(d,n)=calcule_d()
result=calcule_e()
n=result[0]
e=result[2]
public = (e, n)
private = (d, n)
if(choose == '1'):
    enc_msg = encrypt(public, message)
    print("Your encrypted message is:", enc_msg)

elif(choose == '2'):
    print("Your decrypted message is:", decrypt(private, message))
else:
    print("You entered the wrong option.")
    print("Thank you for using the RSA Encryptor. Goodbye!")
"""