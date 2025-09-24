from argparse import ArgumentError


def get_binary_from_string(string: str) -> int:
    if string == "0":
        return 0
    elif string == "1":
        return 1
    else:
        raise ArgumentError(None, "String not recognized")

def get_string_from_binary(binary: int) -> str:
    if binary == 0:
        return "0"
    elif binary == 1:
        return "1"
    else:
        raise ArgumentError(None, "Binary not recognized")