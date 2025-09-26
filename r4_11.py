from bits_operations import *

def l1_11(l0_11: str, k0_11: str, r0_11) -> str:
    f = bits_or(l0_11, k0_11)
    return bits_xor(f, r0_11)

def r1_11(l0_11: str) -> str:
    return l0_11

def k1_11(k0_12: str) -> str:
    return k0_12

def k3_11(k0_14: str) -> str:
    return k0_14

def l2_11(k0_12: str, l0_11: str, k0_11: str, r0_11: str) -> str:
    f = bits_or(k1_11(k0_12), l1_11(l0_11, k0_11, r0_11))
    return bits_xor(f, r1_11(l0_11))

def r2_11(l0_11: str, k0_11: str, r0_11: str) -> str:
    return l1_11(l0_11, k0_11, r0_11)

def l3_11(k0_14: str, k0_12: str, l0_11: str, k0_11: str, r0_11: str) -> str:
    f = bits_or(k3_11(k0_14), l2_11(k0_12, l0_11, k0_11, r0_11))
    return bits_xor(f, r2_11(l0_11, k0_11, r0_11))

def r3_11(k0_12: str, l0_11: str, k0_11: str, r0_11: str) -> str:
    return l2_11(k0_12, l0_11, k0_11, r0_11)

def r4_11(k0_14: str, k0_12: str, l0_11: str, k0_11: str, r0_11: str) -> str:
    f = bits_or(k3_11(k0_14), l3_11(k0_14, k0_12, l0_11, k0_11, r0_11))
    return bits_xor(f, r3_11(k0_12, l0_11, k0_11, r0_11))