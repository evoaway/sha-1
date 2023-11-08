import struct


def padding(message):
    padded_message = message + b'\x80'
    while len(padded_message) % 64 != 56:
        padded_message += b'\x00'
    padded_message += struct.pack('>Q', len(message) * 8)
    return padded_message


def split_into_chunks(message, size):
    return [message[i:i + size] for i in range(0, len(message), size)]


def left_rotate(numb, bit):
    return ((numb << bit) | (numb >> (32 - bit))) & 0xFFFFFFFF


def get_digest(message):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    padded_message = padding(message)
    # print(padded_message)
    chunk_512 = split_into_chunks(padded_message, 64)
    for chunk in chunk_512:
        words = list(struct.unpack(">16I", chunk)) + [0] * 64
        for j in range(16, 80):
            words[j] = left_rotate((words[j - 3] ^ words[j - 8] ^ words[j - 14] ^ words[j - 16]), 1)
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
            a, b, c, d, e = ((left_rotate(a, 5) + f + e + k + words[j]) & 0xFFFFFFFF,
                             a, left_rotate(b, 30), c, d)
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
    return struct.pack('>5I', h0, h1, h2, h3, h4)


def get_hex(message):
    return get_digest(message).hex()
