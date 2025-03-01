from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            print(f"mid: {mid}, left: {left}, right: {right}")

            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:  # Left half is sorted
                if nums[left] <= target < nums[mid]:  # Target in left half
                    right = mid - 1
                else:  # Target in right half
                    left = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[right]:  # Target in right half
                    left = mid + 1
                else:  # Target in left half
                    right = mid - 1
        
        return -1
