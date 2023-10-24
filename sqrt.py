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
        
        # decimal_points = 1 / 12
        left, right = 0.0, float(x)
        TOLERANCE = 1e-12

        if right < 1:
            right = 1
        
        while left <= right:
            mid = (left + (right - left) / 2)  #instead of //, you should use / for float
            square = mid * mid      # always try to define variables

            if abs(square - x) < TOLERANCE:  # Check for precision up to 12 decimal points
                left = mid
            else:
                right = mid

        return round(left, 12) # python built_in, round to certain decimal points. Here we return the left end of the roudning
    
    def sqrt_fast(self, x):
        # write your code here
        left = 0.
        right = 1. + x

        for _ in range(100):
            mid = (left + right) * 0.5
            if mid**2 <= x:
                left = mid
            else:
                right = mid
        
        return left
    
    def sqrt_nice(self, x):
        # write your code here
        # if x < 1, we should use 1 as right
        start, end = 0, max(1, x)
        
        # 1e-12: 0.000000000001
        eps = 1e-12
        
        while start + eps < end:
            mid = start + (end - start) / 2
            if mid * mid + eps < x:
                start = mid
            else:
                end = mid
        
        return start
    def sqrt_in_progress(self, x):
        # write your code here
        if x == 0:
            return 0
        
        # decimal_points = 1 / 12
        left, right = 0.0, float(x)
        TOLERANCE = 1e-12

        if right < 1:
            right = 1
        
        while left <= right:
            mid = (left + (right - left) / 2)  #instead of //, you should use / for float
            square = mid * mid      # always try to define variables

            if abs(square - x) < TOLERANCE:  # Check for precision up to 12 decimal points
                return round(mid, 12) # this is not right!
            elif square < x:        # the square here decide if we move left or right
                left = mid
            else:
                right = mid

        return round(left, 12) 
    
"""
Comment on sqrt_fast():
The `sqrt_fast` function has better runtime than the `sqrt_def` function because it employs a more straightforward and iterative approach to finding the square root.

Here's why `sqrt_fast` is faster:

1. **Iterations:** The `sqrt_fast` function uses a fixed number of iterations (100 in this case) to approach the square root. It doesn't rely on a loop that continues until a specific tolerance is met. This fixed number of iterations ensures that the function runs quickly and doesn't depend on the value of `x`.

2. **Operations:** In `sqrt_fast`, you are performing a limited number of basic arithmetic operations (`+`, `*`, and `<=`). The computation in each iteration is simple and predictable.

3. **Simplified Loop Condition:** Instead of repeatedly checking the difference between `square` and `x` to see if it's within a tolerance (as done in `sqrt_def`), `sqrt_fast` directly checks if `mid**2` is less than or equal to `x`. This condition simplifies the loop and is more efficient.

While `sqrt_fast` may not be as accurate as `sqrt_def` due to a fixed number of iterations, it is faster because it uses a simpler and less computationally intensive approach. Depending on your application, you can choose between these functions based on your requirements for accuracy and runtime.
"""
# Example usage:
# solution = Solution()
# result = solution.sqrt(2.0)
# print(result)  # Output should be approximately 1.414213562373


        
new_solution = Solution()
x = 2
result = new_solution.sqrt_fast(x)
print("result", result)