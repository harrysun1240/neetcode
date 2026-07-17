class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for c in tokens:
            if c == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
            elif c == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif c == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a * b)
            elif c == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b / a))
            else:
                stack.append(c)
        
        return int(stack[0])
