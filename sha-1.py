import struct


def padding(self):
    self.message += b'\x08'
    while len(self.message) % 64 != 56:
        self.message += b'\x00'
    self.message += len(self.message).to_bytes(8, byteorder='big')

def split_into_chunks(self, size):
    chunks, chunk_size = len(self.message), len(self.message) // self.big_chunk_size
    return [self.message[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

def left_rotate(numb, bit):
    return ((numb << bit) | (numb >> (32 - bit))) & 0xFFFFFFFF

def getHexHash(self):
    h0 = 0x67452301,
    h1 = 0xEFCDAB89,
    h2 = 0x98BADCFE,
    h3 = 0x10325476,
    h4 = 0xC3D2E1F0,
    self.padding()
    chunk_512 = self.split_into_chunks(self.big_chunk_size)
    for chunk in chunk_512:
        words = self.split_into_chunks(self.big_chunk_size)
        for word in words:
            new_word = list(struct.unpack(">16L", word)) + [0] * 64
            for j in range(16, 80):
                new_word[j] = left_rotate((word[j - 3] ^ word[j - 8] ^ word[j - 14] ^ word[j - 16]), 1)
            a = h0
            b = h1
            c = h2
            d = h3
            e = h4
            for j in range(80):
                if 0 <= j <= 19:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= j <= 39:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= j <= 59:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= j <= 79:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6
                a, b, c, d, e = ((left_rotate(a, 5) + f + e + k + new_word[j]) & 0xffffffff,
                                 a, left_rotate(b, 30), c, d)
            h0 = (h0 + a) & 0xffffffff
            h1 = (h1 + b) & 0xffffffff
            h2 = (h2 + c) & 0xffffffff
            h3 = (h3 + d) & 0xffffffff
            h4 = (h4 + e) & 0xffffffff
