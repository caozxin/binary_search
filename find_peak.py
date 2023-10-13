from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.

    description: There is an integer array which has the following features:
        The numbers in adjacent positions are different.
        A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
        We define a position P is a peak if:
            A[P] > A[P-1] && A[P] > A[P+1]

    A = [1, 2, 1, 3, 4, 5, 7, 6]
    Ouput = 1 or 6 (return the index of the peak element)

    A = [1,2,3,4,1]
    Output = 3 

    """
    def find_peak(self, a: List[int]) -> int:
        # write your code here
        nums = a
        left, right = 0, len(nums) - 1
        top = -1
        top_idx = 0

        while left < right: # it has to be left < right here! because when they become equal, it indicates that you've found the mountain top.
            mid = left + (right - left) // 2  # Calculate the middle index to avoid overflow. 
            #And it will be updated when there is any change to left or right

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                print("I find it")
                top = nums[mid] 
                top_idx = mid

            if nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1] : # this decdieds when to move right or left
                left = mid + 1 # continue to right half
            else:
                right = mid  # continue to left half

        return top_idx

new_solution = Solution()
A = [1, 2, 1, 3, 4, 5, 7, 6]
A02 = [1,2,3,4,1]
A03 = [1,2,1,4, 1]
result = new_solution.find_peak(A03)
print("top, top_idx", result)
