class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num in d:
                d[num] = d[num] + 1
            else:
                d[num] = 1
        temp = sorted(d.items(), key=lambda x: x[1], reverse=True)
        ret = []
        for i in range(k):
            ret.append(temp[i][0])
        return ret
