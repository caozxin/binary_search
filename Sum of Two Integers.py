class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # Mask to get the last 32 bits

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # Handle overflow for negative numbers
        if a & (1 << 31):
            return ~(a ^ mask)
        else:
            return a
