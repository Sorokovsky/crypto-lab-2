from feistel_encryptor import *
from feistel_analyzer import *
from utils import *
from parser import *

def generate_all_keys() -> list[str]:
    keys = []
    for i in range(65536):
        binary = format(i, "016b")
        keys.append(binary)
    return keys

def key_bits():
    rows = collect_rows()
    analyzer = FeistelAnalyzer(rows)
    encryptor = FeistelEncryptor()
    original_differences = analyzer.collect_differences(analyzer.generate_stats())
    keys = []
    for i in range(2):
        for j in range(2):
                k0_3 = get_string_from_binary(i)
                k0_4 = get_string_from_binary(j)
                key = f"11{k0_3}{k0_4}101011110101"
                keys.append(key)
    max_common_index = 0
    max_common = 0
    for j in range(len(keys)):
        key = keys[j]
        new_rows = []
        for row in rows:
            parts = row.split(";")
            plain = parts[0]
            encrypted = encryptor.encrypt(plain, key)
            new_rows.append(f"{plain};{encrypted}")
        analyzer = FeistelAnalyzer(new_rows)
        new_differences = analyzer.collect_differences(analyzer.generate_stats())
        common_count = 0
        for i in range(len(new_differences)):
            if new_differences[i] == original_differences[i]:
                common_count += 1
        if max_common < common_count:
            max_common = common_count
            max_common_index = j
    k0_3 = keys[max_common_index][2]
    k0_4 = keys[max_common_index][3]
    print(f"Максимально схожа поява бітів із вхідними шифротексті = {max_common} з k0_4 = {k0_3}; k0_4 = {k0_4}")



def main():
    rows = collect_rows()
    encryptor = FeistelEncryptor()
    key = "1111101011110101"
    print(f"Ключ: {key}")
    for row in rows:
        parts = row.split(";")
        plain = parts[0]
        ciphertext = parts[1]
        encrypted = encryptor.encrypt(plain, key)
        if encrypted != ciphertext:
            print("Не правильний")
            return
    print("Правильний")

if __name__ == '__main__':
    main()