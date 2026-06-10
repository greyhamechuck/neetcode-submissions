class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            current = temperatures[i]
            while stack and current > temperatures[stack[-1]]:
                time = i - stack[-1]
                pivot = stack.pop()
                result[pivot] = time

            stack.append(i)

        
        return result