class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = ["+","-","*","/"]
        result = 0
        for char in tokens:
            if char in oper:
                first = int(stack.pop())   
                second = int(stack.pop())              
                if char == "+":
                    stack.append(second + first)
                elif char == "-":
                    stack.append(second - first)
                elif char == "*":
                    stack.append(second * first)
                elif char == "/":
                    stack.append(int(second / first))            
            else:
                stack.append(char)
        
        return int(stack[0])
