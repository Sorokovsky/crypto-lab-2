def bit_or(first: str, second: str) -> str:
    if first == "1" or second == "1":
        return '1'
    else:
        return '0'

def bit_and(first: str, second: str) -> str:
    if first == "1" and second == "1":
        return '1'
    else:
        return '0'

def bit_xor(first: str, second: str) -> str:
    if first == "1" and second == '0':
        return '1'
    elif first == '0' and second == '1':
        return '1'
    else:
        return '0'