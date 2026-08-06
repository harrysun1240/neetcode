class TimeMap:
    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.dictionary.get(key, [])
        lo, hi = 0, len(values) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return res
