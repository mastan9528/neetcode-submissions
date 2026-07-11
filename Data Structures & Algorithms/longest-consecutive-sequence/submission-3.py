class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set()
        for n in nums:
            st.add(n)

        maxi = 0
        for n in nums:
            cnt = 1
            if n-1 in st:
                continue
            else:
                x = n+1
                while x in st:
                    cnt +=1
                    x = x+1
                maxi = max(maxi , cnt)

        return maxi
        