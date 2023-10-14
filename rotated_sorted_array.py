from typing import (
    List,
)

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array

    description: Suppose a sorted array in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element.

    Input:[4, 5, 6, 7, 0, 1, 2]
    Output: 0
    Explanation:
    The minimum value in an array is 0.

    Input:[2,1]
    Output:1
    Explanation:
    The minimum value in an array is 1.
    """
    def find_min(self, nums: List[int]) -> int:
        # write your code here
        # if len(nums) <= 2 and len(nums) > 0:
        #     return min(nums)

        left, right = 0, len(nums) - 1
        botton = float('inf')

        while left < right: # it has to be left < right here! because when they become equal, it indicates that you've found the mountain top.
            mid = left + (right - left) // 2  # Calculate the middle index to avoid overflow. 

            if nums[mid] <  botton:
                print("I find it")
                botton = nums[mid] 
                print("nums[left]", nums[left])

            if nums[mid] > nums [right]: # this decdieds when to move right or left, and nums[mid] > nums[mid + 1]
                left = mid + 1 # continue to right half
            else:
                right = mid  # continue to left half

        return nums[left]
    

    def findMin_default(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1          # 左闭右闭区间，如果用右开区间则不方便判断右值
        while left < right:                     # 循环不变式，如果left == right，则循环结束
            mid = (left + right) >> 1           # 地板除，mid更靠近left
            if nums[mid] > nums[right]:         # 中值 > 右值，最小值在右半边，收缩左边界
                left = mid + 1                  # 因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
            elif nums[mid] < nums[right]:       # 明确中值 < 右值，最小值在左半边，收缩右边界
                right = mid                     # 因为中值 < 右值，中值也可能是最小值，右边界只能取到mid处
        return nums[left]                       # 循环结束，left == right，最小值输出nums[left]或nums[right]均可

    def findMin_classic(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = -1
        target = nums[-1]

        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle index to avoid overflow. 
            #And it will be updated when there is any change to left or right

            if nums[mid] == target:
                result = mid 
                break # if look for 1st index of target, set right = mid - 1 to continue the search on left half
                        # if look for last index of target, set left = mid + 1 to continue the search on right half
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result
new_solution = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
nums02 = [2,0,1]
nums03 = [1, 3, 5]
nums04 = [2, 1]
nums05 = [4,5,6,7,8,9,1,2,3]
nums06 = [6,1,2,3,4,5]
result = new_solution.find_min(nums04)
print("result", result)