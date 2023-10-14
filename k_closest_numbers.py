from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array

    descriptioin: Given target, a non-negative integer k and an integer array A sorted in ascending order, 
    find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. 
    Otherwise, sorted in ascending order by number if the difference is same.

    runtime could be O(logn + k) time.

    Input: A = [1, 2, 3], target = 2, k = 3
    Output: [2, 1, 3]

    Input: A = [1, 4, 6, 8], target = 3, k = 3
    Output: [4, 1, 6]
    """
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        # write your code here
        # find abs(a - target) store it in a dict{}
        #sort it based on the dict{} -->binary search: go left, right, stay
        #return only [:k]
        abs_diff = dict()

        for each in a:
            
            abs_diff[each] = abs(each - target)

        print("abs_diff", abs_diff)
        

        result_list = []
        target_left, target_right = self.target_interval_pointers(a,target)
        print(target_left, target_right)

        # if target_left == target_right and target_left == 0:
        #     return a[target_left:target_left + k ]
        # elif target_left == target_right and target_left != 0:
        #     result = a[target_right + 1 - k: target_right+1]
        #     result.reverse()
        #     return result


        # while len(result_list) < k:
        #     if target_left >= 0 and target_right < len(a):
        #         if abs(a[target_left] - target) < abs(a[target_right] - target):
        #             result_list.append(a[target_left])
        #             target_left -= 1
        #         if abs(a[target_left] - target) == abs(a[target_right] - target):
        #             result_list.append(a[target_left])
        #             target_left -= 1
        #             # result_list.append(a[target_right])
        #             target_right += 1
        #         else:
        #             result_list.append(a[target_right])
        #             target_right += 1
        #     elif target_left >= 0:
        #         result_list.append(a[target_left])
        #         target_left -= 1
        #     elif target_right < len(a):
        #         result_list.append(a[target_right])
        #         target_right += 1

        # print("result_list", result_list)
        # return result_list

        left, right = target_left, target_left + 1
        result = []
        for i in range(k):
            if left < 0:
                result.append(a[right])
                right += 1
            elif right == len(a):
                result.append(a[left])
                left -= 1
            else:
                if target - a[left] <= a[right] - target: 
                    result.append(a[left])
                    left -= 1
                else:
                    result.append(a[right])
                    right += 1
                    
        return result



            

    
    def target_interval_pointers(self, a: List[int], target: int):

        left, right = 0, len(a) - 1
        target_left, target_right = -1, -1
        while left <= right:
            
            mid = left + (right - left) // 2  # Calculate the middle index to avoid overflow. 

            if a[mid] == target:
                target_left, target_right = mid, mid
                break
            elif a[mid] < target:
                target_left = mid
                left = mid + 1
            else:
                target_right = mid
                right = mid - 1
        
        if target_left > target_right:
            target_left, target_right = target_left, target_left

            
        # print(target_left, target_right)
        target_interval = a[target_left: target_right+1]
        print(target_interval)

        return target_left, target_right

    
        
new_solution = Solution()
# A = [1, 4, 6, 8]
# target = 3
# k = 3
# A = [1,4,6,10,20]
# target = 21
# k = 5
# A = [1,10,15,25,35,45,50,59]
# target = 30
# k = 7
A = [1, 2, 3]
target = 2
k = 3
result = new_solution.k_closest_numbers(A, target, k)
print("result", result)