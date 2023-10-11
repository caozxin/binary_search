from typing import List

class Solution:
    """
    implement binary search for a list of integers and return the index of the target from the search. 
    """
    def __init__(self) -> None:
        self.mid = 0
        pass

    def binary_search(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:  # <= because left and right could point to the same element, < would miss it
            mid = (left + right) // 2 # double slash for integer division in python 3, we don't have to worry about integer `left + right` overflow since python integers can be arbitrarily large
            # found target, return its index
            if arr[mid] == target:
                return mid
            # middle less than target, discard left half by making left search boundary `mid + 1`
            if arr[mid] < target:
                left = mid + 1
            # middle greater than target, discard right half by making right search boundary `mid - 1`
            else:
                right = mid - 1
        return -1 # if we get here we didn't hit above return so we didn't find target

# if __name__ == '__main__':
#     arr = [int(x) for x in input().split()]
#     target = int(input())
#     res = binary_search(arr, target)
#     print(res)

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
    
    def binary_search_iterative(self, arr: List[int], target: int) -> int:
        nums = arr
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        # 用 start + 1 < end 而不是 start < end 的目的是为了避免死循环
        # 在 first position of target 的情况下不会出现死循环
        # 但是在 last position of target 的情况下会出现死循环
        # 样例：nums=[1，1] target = 1
        # 为了统一模板，我们就都采用 start + 1 < end，就保证不会出现死循环
        while start + 1 < end:
            # python 没有 overflow 的问题，直接 // 2 就可以了
            # java和C++ 最好写成 mid = start + (end - start) / 2
            # 防止在 start = 2^31 - 1, end = 2^31 - 1 的情况下出现加法 overflow
            mid = (start + end) // 2

            # > , =, < 的逻辑先分开写，然后在看看 = 的情况是否能合并到其他分支里
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else: 
                end = mid

        # 因为上面的循环退出条件是 start + 1 < end
        # 因此这里循环结束的时候，start 和 end 的关系是相邻关系（1和2，3和4这种）
        # 因此需要再单独判断 start 和 end 这两个数谁是我们要的答案
        # 如果是找 first position of target 就先看 start，否则就先看 end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1


new_solution = Solution()
input_array = [1, 3, 5, 7, 8]#[1,3,6,8,9,10]
target = 3
result = new_solution.binary_search_iterative(input_array, target)
print("result", result)
