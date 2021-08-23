# coding=utf-8
# AES加密函数（登入时候需要）
from Crypto.Cipher import AES
from base64 import b64encode


def encrypt(secretkey, passowrd):
    BLOCK_SIZE = AES.block_size
    # 不足BLOCK_SIZE的补位(s可能是含中文，而中文字符utf-8编码占3个位置,gbk是2，所以需要以len(s.encode())，而不是len(s)计算补码)
    pad = lambda s: s + (BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s.encode()) % BLOCK_SIZE)
    key = secretkey  # 密钥
    iv = secretkey[0:16]  # 偏移量

    # passowrd = pad(passowrd) 包pycrypto的写法，加密函数可以接受str也可以接受bytess
    passowrd = pad(passowrd).encode()  # 包pycryptodome 的加密函数不接受str
    cipher = AES.new(key=key.encode(), mode=AES.MODE_ECB)
    encrypted_passowrd = cipher.encrypt(passowrd)
    # 进行64位的编码,返回得到加密后的bytes，decode成字符串
    return b64encode(encrypted_passowrd).decode('utf-8')
