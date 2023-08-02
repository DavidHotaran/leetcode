# my solution
class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
        start = 0
        end = len(s) - 1
        ret = ['' for i in s]

        for i in range(len(s)):
            w1 = s[start]
            w2 = s[end]
            if w1 in vowels:
                if w2 not in vowels:
                    while w2 not in vowels:
                        end -= 1
                        w2 = s[end]
                temp = w2
                ret[end] = w1
                ret[start] = temp
                start += 1
                end -= 1
            else:
                ret[i] = w1
                start += 1
        return ''.join(ret)
    
# alternative
class Solution:
    def reverseVowels(self, s: str) -> str:
        lis=['a', 'e', 'i', 'o','u','A','E','I','O','U']
        i=0
        j=len(s)-1
        s=list(s)
        while(i<j):
            if s[i] not in lis:
                i+=1
            if s[j] not in lis:
                j-=1
            if s[i] in lis and s[j] in lis:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        s="".join(s)
        return s