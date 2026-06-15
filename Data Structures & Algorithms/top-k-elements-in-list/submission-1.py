class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        keys = list(freq)        
        vals = list(freq.values())

        res = []
        for i in range(k):
            ind = vals.index(max(vals))
            res.append(keys[ind])
            keys.pop(ind)
            vals.pop(ind)
        return res
