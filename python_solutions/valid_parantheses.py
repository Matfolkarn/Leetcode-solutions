class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = ['(','{','[']
        closing_brackets = [')','}',']']
        brackets_map = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            print(i)
            print(i in opening_brackets)
            if i in opening_brackets:
                stack.append(i)
            elif i in closing_brackets:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != brackets_map[i]:
                    return False
        if len(stack) != 0:
            return False
        return True