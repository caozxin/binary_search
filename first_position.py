from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.

    descriptioin: iven a sorted array (ascending order) and a target number, 
    find the first index of this number in O(logn) time complexity. If the target does not exist, return -1.

    tuple = [1,4,4,5,7,7,8,9,9,10]
    target = 1  
    output = 0

    tuple = [1, 2, 3, 3, 4, 5, 10]
    target = 3
    output = 2
    """
    def binary_search(self, nums: List[int], target: int) -> int:
        # write your code here
        arr = nums
        counter = 0 
        def recursive_helper(arr: List[int], target: int, index: int):
            n = len(arr)
            if n <= 0:      # this is the recursion base case
                return -1
            
            
            mid = n// 2

            if n == 1:
                mid = 0


            if n == 1 and arr[mid] == target:  # this is the recursion exit strategy
                return index + mid

            if arr[mid] >= target:
                return recursive_helper(arr[:mid], target, index )

            if arr[mid] <= target:
                return recursive_helper(arr[mid + 1:], target, index + mid +1)
            
            
            
        
        if arr[0] == target:
                return 0
        return recursive_helper(arr, target, 0)
    
    def binary_search02(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not nums:     
            return -1
        
        left, right = 0 , n-1
        while left + 1 < right:
            mid = (left + right) //2
            if nums[left] < target:
                left = mid
            elif nums[mid] == target:
                right  = mid
            else:
                right = mid

        
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1
    def binary_search_rec(self, arr: List[int], target: int) -> int:

        def recursive_helper(arr: List[int], target: int, index: int):
            n = len(arr)
            if n <= 0:      # this is the recursion base case
                return -1

            mid = n // 2

            if arr[mid] == target:  # this is the recursion exit strategy
                return index + mid
            elif arr[mid] < target:
                return recursive_helper(arr[mid + 1:], target, mid + 1)
            elif arr[mid] > target:
                return recursive_helper(arr[:mid], target, index)
        
        return recursive_helper(arr, target, 0)
    
new_solution = Solution()
input_array = [2,2, 3,4,5,6,8,13,17,18, 18]
target = 18
tuple02 = [1,4,4,5,7,7,8,9,9,10]
target02 = 9
result = new_solution.binary_search_rec(tuple02, target02)
print("result", result)