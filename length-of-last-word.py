class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.strip()
        ret = 0

        for i in word[::-1]:
            if i == " ":
                return ret
            ret += 1
        return ret
