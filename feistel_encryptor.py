from bits_operations import *

class FeistelEncryptor:
    @staticmethod
    def f(left: str, key: str) -> str:
        if len(left) != len(key):
            raise Exception("Length of left and key must be equal")
        return bits_or(left, key)

    def encrypt(self, plain: str, key: str, rounds: int = 4) -> str:
        half = len(plain) // 2
        if half != len(key):
            raise Exception("Length of plain and key must be equal")
        left = plain[:half]
        right = plain[half:]

        for round in range(rounds):
            f = self.f(left, key)
            r = bits_xor(f, right)
            l = left
            key = bits_left_move(key, 1)
            if round < rounds - 1:
                left, right = r, l
            else:
                left, right = l, r

        return left + right