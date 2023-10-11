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
            if n <= 0:
                return -1

            mid = n // 2

            if arr[mid] == target:  # this is the recursion base
                return index + mid
            elif arr[mid] < target:
                return recursive_helper(arr[mid + 1:], target, mid + 1)
            elif arr[mid] > target:
                return recursive_helper(arr[:mid], target, index)
        
        return recursive_helper(arr, target, 0)

new_solution = Solution()
input_array = [1, 3, 5, 7, 8]#[1,3,6,8,9,10]
target = 8
result = new_solution.binary_search_rec(input_array, target)
print("result", result)
