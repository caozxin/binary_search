from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        nums.sort()
        result = []
        left, right = 0, len(nums) - 1

        # Binary search for the first occurrence of target
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        # Start collecting indices from left position
        while left < len(nums) and nums[left] == target:
            result.append(left)
            left += 1
        
        return result
