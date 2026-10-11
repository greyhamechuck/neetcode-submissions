class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        len1 = len(intervals)
        a = newInterval[0]
        b = newInterval[1]
        left,right = [], []
        result = []
        for i in intervals:
            if i[1]<a:
                left.append(i)

            elif i[0]>b:
                right.append(i)
            
            else:
                a = min(a,i[0])
                b = max(b,i[1])

        result= left+ [[a,b]] + right
        return result

