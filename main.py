from feistel_encryptor import *

def generate_all_keys() -> list[str]:
    keys = []
    for i in range(65536):
        binary = format(i, "016b")
        keys.append(binary)
    return keys

def main():
    encryptor = FeistelEncryptor()
    keys = generate_all_keys()
    decrypted = "01010111010111000000000011111110"
    cypher = "00010100111101000111111101001000"
    for key in keys:
        encrypted = encryptor.encrypt(decrypted, key)
        if encrypted == cypher:
            print(key)


if __name__ == '__main__':
    main()

# 01100100110101011110111000010000
# 01100100110101011110111000010000