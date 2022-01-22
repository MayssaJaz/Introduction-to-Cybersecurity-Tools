from pyDes import *
from Crypto.Random import get_random_bytes


class DESCipher(object):

    def __init__(self):
        self.key = get_random_bytes(8)

    def encrypt(self, raw):
        cipher = des(self.key, CBC, "\0\0\0\0\0\0\0\0",
                     pad=None, padmode=PAD_PKCS5)
        return cipher.encrypt(raw.encode())

    def decrypt(self, enc):
        cipher = des(self.key, CBC, "\0\0\0\0\0\0\0\0",
                     pad=None, padmode=PAD_PKCS5)
        return cipher.decrypt(enc)
