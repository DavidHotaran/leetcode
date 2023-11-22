class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""

        for i in range(len(strs[0])):
            letter = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != letter:
                    return ret
            ret += letter
        return ret
