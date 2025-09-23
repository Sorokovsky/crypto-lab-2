from bits_operations import *
from typing import Tuple

stats: list[dict] = []

def collect(file: str = "files/pairs.txt"):
    result = []
    with open(file, "r") as pairs_file:
        content = pairs_file.read()
        rows = content.strip("\n").split("\n")
        for row in rows:
            result.append(row)
    return result

def show_stats(rows: list[str]):
    for row in rows:
        parts = row.split(";")
        cyphertext = parts[1]
        for i in range(len(cyphertext)):
            if len(stats) <= i:
                stats.append({cyphertext[i]: 1})
            else:
                if cyphertext[i] in stats[i]:
                    stats[i][cyphertext[i]] += 1
                else:
                    stats[i][cyphertext[i]] = 1
    for i in range(len(stats)):
        print(f"Співвідношення 1 / 0 у {i + 1} біті зі всіх шифротекстів: {stats[i]['1']} / {stats[i]['0']} = {round(stats[i]['1'] / stats[i]['0'], 3)}")

def l1_11(l0_11: str, k0_11: str, r0_11: str) -> str:
    f = bit_or(l0_11, k0_11)
    return bit_xor(f, r0_11)

def k1_11(k0_12: str) -> str:
    return k0_12

def r1_11(l0_11: str) -> str:
    return l0_11

def l2_11(l0_11: str, k0_11: str, r0_11: str, k0_12: str) -> str:
    f = bit_or(l1_11(l0_11, k0_11, r0_11), k1_11(k0_12))
    return bit_xor(f, l0_11)

def k2_11(k0_13: str) -> str:
    return k0_13

def r2_11(l0_11: str, k0_11: str, r0_11: str) -> str:
    return l1_11(l0_11, k0_11, r0_11)

def k2_11(k0_13: str) -> str:
    return k0_13

def l3_11(l0_11: str, k0_11: str, r0_11: str, k0_12: str, k0_13: str) -> str:
    f = bit_or(l2_11(l0_11, k0_11, r0_11, k0_12), k2_11(k0_13))
    return bit_xor(f, r2_11(l0_11, k0_11, r0_11))

def generate_stats_by_l4_11(k0_11: str, k0_12: str, k0_13) -> list[str]:
    rows = collect()
    result = []
    for row in rows:
        parts = row.split(";")
        cyphertext = parts[1]
        plainttext = parts[0]
        l0_11 = cyphertext[10]
        r0_11 = cyphertext[10 + 16]
        new_row = f"{plainttext};{l3_11(l0_11, k0_11, r0_11, k0_12, k0_13)}"
        result.append(new_row)
    return result

def shift_left(key: str, i: int) -> str:
    """Циклічний зсув вліво на i."""
    i = i % len(key)
    return key[i:] + key[:i]

def f(right: str, subkey: str) -> str:
    """f(R, Ki) = R | Ki (посимвольно)."""
    return "".join(bit_or(r, k) for r, k in zip(right, subkey))

def feistel_encrypt_block(block: str, key: str, rounds: int = 4) -> str:
    assert len(block) == 32
    assert len(key) == 16

    L, R = block[:16], block[16:]

    for i in range(rounds):
        Ki = shift_left(key, i)        # підключ
        F = f(R, Ki)                   # f(R, Ki)
        new_R_bits = []
        for j in range(16):
            new_R_bits.append(bit_xor(L[j], F[j]))
        new_R = "".join(new_R_bits)
        new_L = R
        L, R = new_L, new_R

    return L + R

# Розшифрування одного блоку
def feistel_decrypt_block(block: str, key: str, rounds: int = 4) -> str:
    assert len(block) == 32
    assert len(key) == 16

    L, R = block[:16], block[16:]

    for i in reversed(range(rounds)):
        Ki = shift_left(key, i)        # той самий підключ
        F = f(L, Ki)                   # тут міняємо порядок
        old_L_bits = []
        for j in range(16):
            old_L_bits.append(bit_xor(R[j], F[j]))
        old_L = "".join(old_L_bits)
        old_R = L
        L, R = old_L, old_R

    return L + R

# Шифрування довільного тексту (кратного 32)
def feistel_encrypt(text: str, key: str) -> str:
    assert len(text) % 32 == 0
    result = []
    for i in range(0, len(text), 32):
        block = text[i:i+32]
        result.append(feistel_encrypt_block(block, key))
    return "".join(result)

def feistel_decrypt(text: str, key: str) -> str:
    assert len(text) % 32 == 0
    result = []
    for i in range(0, len(text), 32):
        block = text[i:i+32]
        result.append(feistel_decrypt_block(block, key))
    return "".join(result)

def get_binary(number: int) -> str:
    if number == 0:
        return "0"
    else:
        return "1"

def generate_keys():
    keys = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        for n in range(2):
                            for o in range(2):
                                for p in range(2):
                                    for q in range(2):
                                        for r in range(2):
                                            for s in range(2):
                                                for t in range(2):
                                                    for u in range(2):
                                                        k0 = get_binary(i)
                                                        k1 = get_binary(j)
                                                        k2 = get_binary(k)
                                                        k3 = get_binary(l)
                                                        k4 = get_binary(m)
                                                        k5 = get_binary(n)
                                                        k6 = get_binary(o)
                                                        k7 = get_binary(p)
                                                        k8 = get_binary(q)
                                                        k9 = get_binary(r)
                                                        k10 = get_binary(0)
                                                        k11 = get_binary(0)
                                                        k12 = get_binary(0)
                                                        k13 = get_binary(s)
                                                        k14 = get_binary(t)
                                                        k15 = get_binary(u)
                                                        keys.append(f"{k0}{k1}{k2}{k3}{k4}{k5}{k6}{k7}{k8}{k9}{k10}{k11}{k12}{k13}{k14}{k15}")

    return keys

def main():
    rows = collect()
    parts = rows[0].split(";")
    keys = generate_keys()
    cyphertext = parts[1]
    plainttext = parts[0]
    for i in range(len(keys)):
        encrypted = feistel_encrypt(plainttext, keys[i])
        if cyphertext == encrypted:
            print(f"Ключ: {keys[i]}")

if __name__ == '__main__':
    print(generate_keys())

# 01010111010111000101011110100010
# 01010111010111000101011110100010