class FeistelAnalyzer:
    def __init__(self, pairs: list[str]) -> None:
        self._pairs = pairs.copy()

    def generate_stats(self):
        stats: list[dict] = []
        for pair in self._pairs:
            parts = pair.split(';')
            cypher = parts[1]
            for i in range(len(cypher)):
                if len(stats) <= i:
                    stats.append({"0": 0, "1": 0})
                stats[i][cypher[i]] += 1
        return stats

    @staticmethod
    def collect_differences(stats: list[dict]) -> list[int]:
        result = []
        zero_index = "0"
        one_index = "1"
        for i in range(len(stats)):
            stat = stats[i]
            result.append(abs(stat[zero_index] - stat[one_index]))
        return result

    @staticmethod
    def show_stats(differences: list[int]) -> None:
        max_index = 0
        for i in range(len(differences)):
            difference = differences[i]
            if abs(differences[max_index]) <= difference:
                max_index = i
            print(f"Абсолютна різниця кількості появи 0, 1 у {i + 1} біті = {difference}")
        print(f"Максимальна абсолютна різниця у {max_index + 1} біті, яка становить {differences[max_index]}")