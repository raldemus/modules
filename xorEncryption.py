import itertools


def xor_encryption(string, key):
    answer = []
    key = itertools.cycle(key)
    for s, k in zip(string, key):
        answer.append(chr(ord(s) ^ ord(k)))
    return ''.join(answer)


print(xor_encryption(input("Enter the string you want to encrypt or decrypt: "),
                     input("Enter the encryption key: ")))
