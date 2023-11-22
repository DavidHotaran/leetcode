class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = p2 = 0

        while p1 <= len(s) - 1 and p2 <= len(t) - 1:
            l1 = s[p1]
            l2 = t[p2]

            if l1 == l2:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return p1 == len(s)
