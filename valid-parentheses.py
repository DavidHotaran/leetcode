class Solution:
    def isValid(self, s: str) -> bool:
        _open = ("(", "{", "[")
        close = (")", "}", "]")
        stack = []

        for paren in s:
            if paren in _open:
                stack.append(paren)
            if paren in close:
                if not stack:
                    return False
                if stack and stack[-1] in _open:
                    if paren == ")" and stack[-1] == "(":
                        stack.pop()
                    elif paren == "]" and stack[-1] == "[":
                        stack.pop()
                    elif paren == "}" and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
