from feistel_encryptor import *
from feistel_analyzer import *
from utils import *

def generate_all_keys() -> list[str]:
    keys = []
    for i in range(65536):
        binary = format(i, "016b")
        keys.append(binary)
    return keys

def main():
    encryptor = FeistelEncryptor()
    analyzer = FeistelAnalyzer(collect_rows())
    stats = analyzer.generate_stats()
    analyzer.show_stats(stats)


if __name__ == '__main__':
    main()

# 01100100110101011110111000010000
# 01100100110101011110111000010000