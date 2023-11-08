import sha1
import hashlib


def tests():
    str = "The quick brown fox jumps over the lazy dog"
    hex = hashlib.sha1(str.encode()).digest()
    print(hex)
    print('\n')
    hex = sha1.get_digest(str.encode())
    print(hex)

if __name__ == '__main__':
    tests()
