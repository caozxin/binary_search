#Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.

from typing import (
    List,
)

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def find_missing(self, nums: List[int]) -> int:
        # write your code here
        n = len(nums)
        left, right = 0, n - 1
        
        while left <= right: 
            mid = left + (right - left) //2
            # print(left, right, mid)
            print("mid, nums[mid]")
            print(mid, nums[mid])
            if nums[mid] < mid:  #move to left
                right = mid - 1
            else: # move to right
                left = mid + 1
            
