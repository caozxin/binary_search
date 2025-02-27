from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left, right = 0, len(nums) - 1
        min_nums = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums [right]:
                left = mid + 1
            else:
                min_nums = min(min_nums, nums[mid])
                right = mid - 1
        return min_nums if min_nums != float('inf') else nums[0]
