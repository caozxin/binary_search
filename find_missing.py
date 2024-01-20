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
        expected_nums = set()
        for each in range(n+1):
            expected_nums.add(each)
        print(expected_nums)

        curr_nums = set(nums)
        result = expected_nums.difference(curr_nums)
        print(result)

        return list(result)[0]


        
            
            

            
