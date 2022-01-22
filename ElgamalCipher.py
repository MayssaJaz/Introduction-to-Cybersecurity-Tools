import base64
from Crypto.Util import number

class ElgamalCipher(object):

    def __init__(self,bits): 
        #generate random prime p
        self.q = number.getPrime(bits-1)
        self.p = self.q *2 -1
        while True:
            self.g = number.getRandomRange(3, self.q+1) 
            #check if (g^i != 1 mod p) for 0 < i < p-1
            for i in range(1, self.q -1):
                if (pow(self.g, i, self.p) == 1):
                    break
            break
        #private key
        self.x = number.getRandomRange(2, self.q -1)

        #public key y = g^x % p
        self.y = pow(self.g, self.x, self.p)

    def encrypt(self, raw):
        k = number.getRandomRange(2, self.p-1)
        #cipher text (g^k%p, my^k%p)
        u = pow(self.g, k, self.p)
        v = ( raw* pow(self.y, k, self.p) ) % self.p
        return u, v

    def decrypt(self, u,v):
        # message v/(u^x) % p
        decrypted = (v * pow(u,-self.x, self.p)) % self.p
        return decrypted
