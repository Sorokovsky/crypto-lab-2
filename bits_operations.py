def bits_or(first: str, second: str) -> str:
    result: list[str] = []
    if len(first) != len(second):
        raise ValueError('First & second must be of same length')

    for i in range(len(first)):
        if first[i] == '1' or second[i] == '1':
            result.append("1")
        else:
            result.append("0")
    return "".join(result)


def bits_and(first: str, second: str) -> str:
    result: list[str] = []
    if len(first) != len(second):
        raise ValueError('First & second must be of same length')

    for i in range(len(first)):
        if first[i] == '1' and second[i] == '1':
            result.append("1")
        else:
            result.append("0")
    return "".join(result)

def bits_xor(first: str, second: str) -> str:
    result: list[str] = []
    if len(first) != len(second):
        raise ValueError('First & second must be of same length')

    for i in range(len(first)):
        if first[i] == '0' and second[i] == '1':
            result.append("1")
        elif first[i] == '1' and second[i] == '0':
            result.append("1")
        else:
            result.append("0")
    return "".join(result)