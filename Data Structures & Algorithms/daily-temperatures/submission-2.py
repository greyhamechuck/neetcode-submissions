class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        temp = [] 
        result = []* n
        for i in range(n-1,-1,-1):
            while temp and temperatures[temp[-1]]<=temperatures[i]:
                temp.pop()

            if temp:
                result.append(temp[-1]-i)
            else:
                result.append(0)

            temp.append(i)
        final = []
        for i in range(n-1,-1,-1):
            final.append(result[i])

        return final