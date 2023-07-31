def reverseWords(s: str) -> str:
        ret = []
        p1 = len(s) - 1
        p2 = len(s) -1

        while p1 >= 0: # keep going until we are at the first word
            while p1 > 0 and s[p1] != ' ': # while we are still going over the string and we are not at a space, decrement p1
                p1 -= 1
            temp = p1 - 1 # keep a place holder to go back to, next word after the space we encountered
            t_s = ''

            while p1 <= p2: # while we still have letters to append
                if s[p1] != ' ':
                    t_s += s[p1]
                p1 += 1 # add 1 to p1 to keep going
            p1 = p2 = temp
            if t_s != '': # need this check bc of line 10, there are scenarios where we only have ' ' to append, which wont happen, so then '' gets appended to the file result.
                ret.append(t_s)
        return ' '.join(ret)

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))