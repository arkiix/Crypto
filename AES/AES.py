from base64 import b64encode, b64decode
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class AESCipher():
    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain):
        plain = pad(plain.encode(), self.bs)
        iv = Random.new().read(self.bs)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(plain))

    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:self.bs]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[self.bs:]), self.bs).decode('utf-8')

cipher = AESCipher('key')
c = cipher.encrypt('Hello, world!')
print(cipher.decrypt(c))