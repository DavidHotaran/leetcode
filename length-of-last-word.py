class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.strip()
        ret = 0

        for i in word[::-1]:
            if i == " ":
                return ret
            ret += 1
        return ret


# Solution 2
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ret = 0
        i = len(s) - 1

        for j in range(i, -1, -1):
            if s[j] != " ":
                break
            i -= 1

        for j in range(i, -1, -1):
            if s[j] == " ":
                break
            ret += 1

        return ret
