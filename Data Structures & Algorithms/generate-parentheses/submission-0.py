class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def parenthesis(opened , closed , ans):

            if len(ans) == 2*n:
                result.append(ans)
                return 

            if opened < n:
                parenthesis(opened+1 , closed , ans+"(")

            if closed < opened:
                parenthesis(opened , closed+1 ,ans+")")

        parenthesis(0,0,"")

        return result