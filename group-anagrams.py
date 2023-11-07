class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            temp = "".join(sorted(word))
            if temp in d:
                d[temp].append(word)
            else:
                d[temp] = [word]

        return d.values()
