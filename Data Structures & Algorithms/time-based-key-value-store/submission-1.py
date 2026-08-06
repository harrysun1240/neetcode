class TimeMap:
    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.dictionary[key]) == 0:
            return ""
        
        lo, hi = 0, len(self.dictionary[key]) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            value = self.dictionary[key][mid]
            if value[0] == timestamp or (
                value[0] < timestamp and self.dictionary[key][mid + 1][0] > timestamp
            ):
                return self.dictionary[key][mid][1]
            elif value[0] > timestamp:
                hi = mid
            else:
                lo = mid + 1
        return self.dictionary[key][lo][1] if timestamp >= self.dictionary[key][lo][0] else ""
