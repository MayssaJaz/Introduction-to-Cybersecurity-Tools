
import base64
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto import Random

class AESCipher(object):

    def __init__(self): 
        self.key = get_random_bytes(16)

    def encrypt(self, raw):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC,iv)
        ciphertext = base64.b64encode( iv + cipher.encrypt( pad(raw.encode(), AES.block_size ) ))
        return ciphertext

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(enc[AES.block_size:])
        return unpad(plaintext, AES.block_size)
