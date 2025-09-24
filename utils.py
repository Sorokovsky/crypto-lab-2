def collect_rows(file_path: str = "files/pairs.txt"):
    with open(file_path, "r") as file:
        result = []
        for line in file:
            row = line.strip()
            result.append(row)
    return result