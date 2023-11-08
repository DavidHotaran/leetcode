class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        total = 0

        for i, el in enumerate(s):
            seen.clear()
            l = i
            r = len(s) - 1
            temp = 0
            while l <= r:
                if s[l] in seen:
                    break
                seen.add(s[l])
                temp += 1
                l += 1
            total = max(temp, total)
        return total
