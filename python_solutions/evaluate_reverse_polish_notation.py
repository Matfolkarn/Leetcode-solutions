class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "*":      
                    stack.append(stack.pop() * stack.pop())
                case "-":
                    v2 = stack.pop()
                    v1 = stack.pop()
                    stack.append(v1 - v2)
                case "/":
                    v2 = stack.pop()
                    v1 = stack.pop()
                    stack.append(int(v1/v2))
                case _:
                    stack.append(int(t))
        return stack[0]
