from feistel_encryptor import *
from feistel_analyzer import *
from utils import *
from parser import *
from r4_11 import *

def generate_all_keys() -> list[str]:
    keys = []
    for i in range(65536):
        binary = format(i, "016b")
        keys.append(binary)
    return keys

def key_bits_for_r4_11():
    encryptor = FeistelEncryptor()
    rows = collect_rows()
    analyzer = FeistelAnalyzer(rows)
    differences = analyzer.collect_differences(analyzer.generate_stats())
    analyzer.show_stats(differences)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                k0_11 = get_string_from_binary(i)
                k0_12 = get_string_from_binary(j)
                k0_14 = get_string_from_binary(k)
                correct = True
                for row in rows:
                    parts = row.split(";")
                    plain = parts[0]
                    cipher = parts[1]
                    l0_11 = plain[10]
                    r0_11 = plain[10 + 16]
                    encrypted = r4_11(k0_14, k0_12, l0_11, k0_11, r0_11)
                    if encrypted != cipher[10 + 16]:
                        correct = False
                if correct:
                    print(f"k0_11: {k0_11}; k0_12: {k0_12}; k0_14: {k0_14};")
    print("======================================================================================")

def main():
    key_bits_for_r4_11()
    keys = generate_all_keys()
    rows = collect_rows()
    parts = rows[0].split(";")
    plain = parts[0]
    cipher = parts[1]
    encryptor = FeistelEncryptor()
    for key in keys:
        encrypted = encryptor.encrypt(plain, key)
        if encrypted == cipher:
            print(f"k0_11: {key[10]}; k0_12: {key[11]}; k0_14: {key[13]};")
    print("======================================================================================")

if __name__ == '__main__':
    main()