from typing import (
    List,
)

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top

    description: Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top(Maximum).

    Input: nums = [1, 2, 4, 8, 6, 3] 
    Output: 8

    Input: nums = [10, 9, 8, 7], 
    Output: 10
    """
    def mountain_sequence(self, nums: List[int]) -> int:
        # write your code here
        left, right = 0, len(nums) - 1
        top = -1
        

        while left >= 0 and right < len(nums) :
            mid = left + (right - left) // 2
            if nums[mid] > top:
                top = nums[mid]
                left = mid
                right = mid + 2
            elif nums[left] < top and nums[right] > top:
                left = mid
                right = mid + 2
            elif nums[left] > top and nums[right] < top:
                left = mid - 2
                right = mid
            else:
                left -= 1
                right += 1

        return top
    
    def mountain_sequence02(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        top = nums[left + (right - left) // 2]

        while left < right: # it has to be left < right here! because when they become equal, it indicates that you've found the mountain top.
            mid = left + (right - left) // 2  # Calculate the middle index to avoid overflow. 
            #And it will be updated when there is any change to left or right

            if nums[mid] > top:
                top = nums[mid] 

            if nums[mid] < nums[mid + 1]: # whether move to right or left, it depends on the nums[mid] and nums[mid + 1]
                left = mid + 1 # continue to right half
            else:
                right = mid  # continue to left half

        return top
    
    def mountain_sequence_default(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        # When the while loop exits, left and right will be equal, indicating the mountain top
        return nums[left]

new_solution = Solution()
nums = [1, 2, 4, 8, 10, 6, 3] #[10, 9, 8, 7] #
result = new_solution.mountain_sequence02(nums)
print("result", result)