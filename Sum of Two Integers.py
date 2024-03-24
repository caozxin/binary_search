class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF  # Mask to get the last 32 bits --> this is to convert any integer into 32- bit format. mask = 0x(F*8)

        if a == 0 and b == 0: # if both is zero
            return 0

        while b!= 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # Handle overflow for negative numbers
        # if a & (1 << 31): 
        #     return ~(a ^ mask)
        # else:
        #     return a

        if a < 0x80000000: # The operation 'a < 0x80000000' checks if the result is within the positive range
        # of a 32-bit integer (from 0x00000000 to 0x7FFFFFFF)
            return a
        else:
            # If a is outside the 32-bit integer range, which means it is negative,
            # return the two's complement negative value, which is the bitwise negation of a
            # (by XORing with MASK, which is 'all 1's for a 32-bit number') and adding 1
            return ~(a ^ mask)

