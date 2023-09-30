from typing import (
    List,
)

from collections import deque

class Solution:
    """
    description:
    Find the last position of a target number in a sorted array. Return -1 if target does not exist.

    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer

    Input: nums = [1,2,2,4,5,5], target = 2
    Output: 2

    Input: nums = [1,2,2,4,5,5], target = 6
    Output: -1

    """
    def last_position(self, nums: List[int], target: int) -> int:
        # write your code here
        
        n = len(nums)
        
        if (type(target) != int) or (n <= 0): # check if nothing in the target 
            # print("no target", type(target))
            return -1
        
        if target not in nums:
            return -1
        
        if target == nums[0]:
            return 0
        
        if nums[0] > target or nums[n-1] < target: # becuase the input numbers is sorted, we check the min and max with the target
            return -1
        min_idx = 0
        max_idx = n
        mid_point = n//2 
        block = ""
        if nums[mid_point] > target:  #adding mid point to check where the target belongs to
            max_idx = mid_point
            block = "left"
        elif nums[mid_point] <= target: 
            min_idx = mid_point
            block = "right"

        print("mid_point", mid_point)
        # loop in reverse order:
        updated_nums = nums[min_idx:max_idx] # we should use slice here
        print("updated_nums", updated_nums)

        for i in range(len(updated_nums)-1, -1, -1):
            # print(i) # always first check if the iteration order is working as expected
            if updated_nums[i] == target:
                print("find the target", i)
                print(block)
                if block == "right":
                    print(i + mid_point)
                    return i + mid_point
                else: 
                    print(i)
                    return i

        return -1

    def last_position02(self, nums: List[int], target: int) -> int:
        # write your code here
        # because the nums is sorted, we can use bineary search O(logN)
        n = len(nums)
        
        if (type(target) != int) or (n <= 0): # check if nothing in the target 
            # print("no target", type(target))
            return -1
        if target not in nums:
            return -1
        
        if nums[0] > target or nums[n-1] < target: # becuase the input numbers is sorted, we check the min and max with the target
            return -1

        # Set to keep track of visited positions
        visited = 0
        num_of_iteration = 0

        
        while len(nums) > 0:
            m = len(nums)
            num_of_iteration += 1 
            
            # visited.add(idx)
            mid_point = m//2 
            if visited == 0:
                visited = mid_point
            print("mid_point", mid_point)
            print("visited", visited)
            print("current num", nums[mid_point])

            # print(m, nums, num_of_iteration, mid_point)
            print("num_of_iteration, mid_point")
            print(num_of_iteration, mid_point)
            
            # Check if the current position is within the bounds
            if 0 <= num_of_iteration < n:
                if nums[mid_point] > target:  #moving to left
                    block = "left"
                    # visited.append(mid_point)
                    
                    nums = nums[:mid_point]
                    mid_point = len(nums) //2
                    visited -= mid_point

                elif nums[mid_point] < target: #moving to right
                    block = "right"
                    # visited.append(mid_point)
                    
                    nums = nums[mid_point:]
                    mid_point = len(nums) //2
                    visited += mid_point

                else:
                    print("find the target")
                    print(visited)

                    return visited


        

new_solution = Solution()
nums = [1,2,3,4,5]
target = 3

new_solution.last_position02(nums, target)