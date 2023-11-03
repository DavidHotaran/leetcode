class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ret = temp = 0

        for i in gain:
            temp += i
            ret = max(temp, ret)
        return ret
