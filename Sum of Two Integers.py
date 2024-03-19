#Given two integers a and b, return the sum of the two integers without using the operators + and -.

 class Solution:
    def getSum(self, a: int, b: int) -> int:
        if not a or not b:
            return 0

        max_val = max(a,b)
        min_val = min(a,b)
        result_list = []
        
        for i in range(max_val):
            print(i)
            result_list.append(i)

        for j in range(min_val):
            print(j)
            result_list.append(j)

        print(len(result_list))
        return len(result_list)

