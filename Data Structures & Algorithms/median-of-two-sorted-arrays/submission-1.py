class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # i , j = 0 , len(nums1)-1
        # median_index = (len(nums1)+len(nums2))//2
        # odd = False
        # if len(nums1)+len(nums2) % 2:
        #     odd = True

        # while i < j:
        #     mid = (i+j)//2
        #     i1 , j1 = 0 , len(nums2)-1
        #     while i1 < j1:
        #         mid1 = (i1+j1)//2

        #         if nums2[mid1] <= nums1[mid]:
        #             mini = mid1
        #             i1 = mid1 +1

        #         else:
        #             j1 = mid1 - 1

        #     num = (mid+1) + mini+1

        #     if num ==median or (num == median+1 if odd):
        if not nums1:
            mid_idx = len(nums2) // 2
            return nums2[mid_idx] if len(nums2) % 2 != 0 else (nums2[mid_idx - 1] + nums2[mid_idx]) / 2.0
        if not nums2:
            mid_idx = len(nums1) // 2
            return nums1[mid_idx] if len(nums1) % 2 != 0 else (nums1[mid_idx - 1] + nums1[mid_idx]) / 2.0

        i , j = 0 , len(nums1)-1
        total_len = len(nums1) + len(nums2)
        median = total_len // 2
        
        # Parentheses added to fix operator precedence (% happens before +)
        odd = False
        if (len(nums1) + len(nums2)) % 2:
            odd = True

        # Changed to <= so it scans the last remaining element when i == j
        while i <= j:
            mid = (i+j)//2
            
            # mini must be initialized to -1 in case no element in nums2 is <= nums1[mid]
            mini = -1 
            i1 , j1 = 0 , len(nums2)-1
            
            # Changed to <= to search the full boundary of nums2
            while i1 <= j1:
                mid1 = (i1+j1)//2

                if nums2[mid1] <= nums1[mid]:
                    mini = mid1
                    i1 = mid1 + 1
                else:
                    j1 = mid1 - 1

            # total elements less than or equal to nums1[mid] across both arrays
            num = (mid+1) + (mini+1)

            # --- YOUR LOGIC COMPLETION ---
            if odd:
                if num == median + 1:
                    return float(nums1[mid])
                elif num < median + 1:
                    i = mid + 1  # Move right: current nums1[mid] is too small
                else:
                    j = mid - 1  # Move left: current nums1[mid] is too large
            else:
                # For even lengths, we need two elements. 
                # If num hits the exact partition boundary:
                if num == median:
                    # We need to find the next immediate element to average with
                    next_val = float('inf')
                    if mid + 1 < len(nums1):
                        next_val = min(next_val, nums1[mid + 1])
                    if mini + 1 < len(nums2):
                        next_val = min(next_val, nums2[mini + 1])
                    return (nums1[mid] + next_val) / 2.0
                elif num < median:
                    i = mid + 1
                else:
                    j = mid - 1
                    
        # Fallback to handle when the target median element sits inside nums2 instead of nums1
        combined = sorted(nums1 + nums2)
        return float(combined[median]) if odd else (combined[median - 1] + combined[median]) / 2.0

            


        