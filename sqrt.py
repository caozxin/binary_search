class Solution:
    """
    @param x: a double
    @return: the square root of x
    description: given x is >= 0, return the square root of x ups to 12 decimal points --> which means we need to at least divide it by 12 times
    """
    def sqrt(self, x):
        # write your code here
        if x == 0:
            return 0
        
        decimal_points = (0.1)** 2
        print(decimal_points)
        step = decimal_points
        target_x = x * ((10) ** 2)
        left, right = 0.00, float(x)
        print(target_x)
        # mid = (right + left) //2
        multiplier = 10**decimal_points


        while left <= right: 
        
            result = float('inf')
            mid = round((left + (right - left) // 2 ) * multiplier, ndigits=12)
            
            if mid * mid <= x:
                if x - (mid * mid) <= 0.001:
                    return mid
                left = mid 
            else:
                right = mid 

        return left
    

    def sqrt_def(self, x):
        if x == 0:
            return 0
        
        decimal_points = 1 / 12
        left, right = 0.0, float(x)
        
        while left <= right:
            mid = (left + (right - left) / 2)
            square = mid * mid

            if abs(square - x) < 1e-12:  # Check for precision up to 12 decimal points
                return round(mid, 12)
            elif square < x:
                left = mid
            else:
                right = mid

        return round(left, 12)

# Example usage:
# solution = Solution()
# result = solution.sqrt(2.0)
# print(result)  # Output should be approximately 1.414213562373


        
new_solution = Solution()
x = 2
result = new_solution.sqrt_def(x)
print("result", result)