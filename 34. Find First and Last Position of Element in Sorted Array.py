class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if not nums:
        #     return [-1, -1]

        left, right = 0, len(nums) - 1
        first_idx, last_idx = -1, -1
        result = []

        while left <= right:
            mid = (left + right) // 2
            print("mid", mid, left, right)
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        # print("mid", mid, left, right)

        # Start collecting indices from left position
        while left < len(nums) and nums[left] == target:
            result.append(left)
            left += 1
        print(result)
        # if len(result) == 1:
        #     return [result[0], result[0]]
        return [result[0], result[-1]] if result else [-1, -1]
