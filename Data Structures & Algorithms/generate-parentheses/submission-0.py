class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0:
            return res

        path = []

        def back(left,right):
            if left == n and right == n:
                res.append("".join(path.copy()))

            if left<n:
                path.append("(")
                back(left+1,right)
                path.pop()

            if right<left:
                path.append(")")
                back(left,right+1)
                path.pop()


        back(0,0)
        return res