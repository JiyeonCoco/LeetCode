class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        int_stack = []

        for t in tokens:
            if t not in '+-*/':
                int_stack.append(int(t))
        
            else:
                n2 = int_stack.pop()
                n1 = int_stack.pop()

                if t == '+':
                    res = n1 + n2
                elif t == '-':
                    res = n1 - n2
                elif t == '*':
                    res = n1 * n2
                elif t == '/':
                    res = int(n1 / n2)
                int_stack.append(res)

        return int_stack[-1]
