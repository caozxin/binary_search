# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # if not n:
        #     return 0

        left, right = 1, n
        res_idx = -1
        while left <= right:
            mid = (left + right) // 2
            # print(f"mid: {mid}, left: {left}, right: {right}")
            if isBadVersion(mid):
                res_idx = mid
                right = mid - 1 # go to left half
            else:
                left = mid + 1 # go to right half
        
        return res_idx
