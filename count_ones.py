#Count how many 1 in binary representation of a 32-bit integer.
class Solution:
    """
    @param num: An integer
    @return: An integer, the number of ones in num
    """
    def count_ones(self, num: int) -> int:
        # Check if num is negative and convert to its positive equivalent
        if num < 0:
            num = 2**32 + num #In Python, the double asterisk ** is used as the exponentiation operator. 
            #It is used to raise a number to the power of another number.

        result = 0
        while num:
            result += num % 2
            num = num >> 1

        return result




        


        


        
