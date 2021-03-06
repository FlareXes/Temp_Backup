import hashlib
from os import urandom
from base64 import b64encode


def password_hasher(password: str) -> tuple:
    try:
        salt = urandom(16)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 150000)
        return b64encode(salt), b64encode(key)
    except Exception as e:
        print(e)
        print("\nāāā ErRoR OcCuRrEd š Unable To Hash The Password āāā")


if __name__ == '__main__':
    print("\nāāā Don't Mess With Internal Files Otherwise You May Loss Your Data āāā")
    print("\nāāā Sorry! You can not run this file directly āāā\n")
    exit()