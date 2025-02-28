class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res_idx = -1

        if not nums:
            return res_idx

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                res_idx = mid
                return res_idx
            elif nums[mid] > target:
                    right = mid - 1
            else:
                left = mid + 1

        return res_idx
