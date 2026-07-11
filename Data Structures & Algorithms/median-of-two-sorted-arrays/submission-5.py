class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1 ,nums2

        total = len(nums1)+ len(nums2)

        half = total //2
        odd = False
        if total % 2:
            odd =   True

        if A and B and len(A) > len(B):
            A , B = B , A

        i , j = 0  , len(A)-1
        ans = -1
        while i <= j:
            mid = (i+j)//2
            mini = -1
            i1 , j1 = 0 , len(B)-1
            while i1 < j1:
                mid1 = (i1+j1)//2

                if B[mid1] <= A[mid]:
                    mini = mid1
                    i1 = mid1+1
                else:
                    j1 = mid1 -1

            val = mid+1 + mini+1
            if val <= half:
                ans = mid
                i = mid+1
            else:
                j =mid-1

        # remaining_len = half - (ans+1)

        # ans_1 = max(A[ans] , B[remaining_len])
        # if not odd:
        #     if len(A) > ans+1 and len(B) > remaining_len:
        #         ans_2 = min(A[ans+1] , B[remaining_len])
        #     elif len(A) > ans+1:
        #         ans_2 = A[ans+1]
        #     else:
        #         ans_2 = B[remaining_len]
        #     return (ans_1 + ans_2) / 2.0
        # return float(ans_1)
        remaining_len = half - (ans + 1)

        left_A = A[ans] if ans >= 0 else float('-inf')
        left_B = B[remaining_len - 1] if remaining_len - 1 >= 0 else float('-inf')
        ans_1 = max(left_A, left_B)

        right_A = A[ans + 1] if ans + 1 < len(A) else float('inf')
        right_B = B[remaining_len] if remaining_len < len(B) else float('inf')
        ans_2 = min(right_A, right_B)

        if odd:
            return float(ans_2)

        return (ans_1 + ans_2) / 2

            


