class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        if not arr:
            return 0

        left, right = 0, len(arr) - 1
        max_arr = float('-inf')
        max_idx = -1
        while left <= right:
            mid = (left + right) // 2
            print("mid", mid, left, right)
            if arr[mid] >= arr[mid + 1]: # only update max_arr when arr[mid]  is the local maximum
                if max_arr <= arr[mid]:
                    max_arr = arr[mid]
                    max_idx = mid
                    print("max_arr", max_arr, max_idx)
                right = mid - 1 # move to left half
            else:
                left = mid + 1 # move to right half
        

        return max_idx if max_idx != -1 else 0
