class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = ["+","-","*","/"]
        number = []
        result = 0
        for token in tokens:
            if token not in oper:
                number.append(token)
            else:
                second = int(number.pop())
                first = int(number.pop())
                if token == "+":
                    result = first+second
                    number.append(result)
                elif token == "-":
                    result=first - second
                    number.append(result)
                elif token == "*":
                    result = first*second
                    number.append(result)
                elif token == "/":
                    result = first / second
                    number.append(result)

        return int(number[0])
