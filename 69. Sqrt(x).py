class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x
        res = -1

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                res = mid # we update res as it gets closer to sqrt of n
                right = mid - 1
            else:
                left = mid + 1
        return res - 1 # unless we find the exact integer of sqrt of n, otherwise we will return the nearest integer that smaller than sqrt of n
