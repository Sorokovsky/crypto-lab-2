from feistel_encryptor import *
from typing import *

class FeistelAnalyzer:
    def __init__(self, pairs: list[str]) -> list[dict]:
        self._pairs = pairs.copy()

    def generate_stats(self):
        stats: list[dict] = []
        for pair in self._pairs:
            parts = pair.split(';')
            cypher = parts[1]
            for i in range(len(cypher)):
                if len(stats) <= i:
                    stats.append({cypher[i]: 1})
                else:
                    if cypher[i] in stats[i]:
                        stats[i][cypher[i]] += 1
                    else:
                        stats[i][cypher[i]] = 1
        return stats

    @staticmethod
    def show_stats(stats: list[dict]) -> None:
        max_index = 0
        for i in range(len(stats)):
            stat = stats[i]
            zero_stat = stat["0"]
            one_stat = stat["1"]
            difference = abs(zero_stat - one_stat)
            if abs(stats[max_index]["0"] - stats[max_index]["1"]) <= difference:
                max_index = i
            print(f"Абсолютна різниця кількості появи 0, 1 у {i + 1} біті = {zero_stat} - {one_stat} = {difference}")
        print(f"Максимальна абсолютна різниця у {max_index + 1} біті, яка становить {abs(stats[max_index]['0'] - stats[max_index]['1'])}")