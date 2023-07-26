class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L = max(len(word1), len(word2))
        ret = ""

        for i in range(L):
            if i < len(word1):
                ret += word1[i]
            if i < len(word2):
                ret += word2[i]
        return ret