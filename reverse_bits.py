#Reverse bits of a given 32 bits unsigned integer.
class Solution:
    """
    @param n: an integer
    @return: return an integer
    """
    def reverse_bits(self, n: int) -> int:
        # write your code here
        # unsigned integer only is non-negative. 
        input_n = n
        print(input_n, type(input_n))

        # convert the number into its binary form:
        binary_representation = format(input_n, '032b')
        print(binary_representation) #binary_representation is a string
        # print(reversed(binary_representation))

        k = len(binary_representation)
        print(k)
        reversed_num = ""
        for i in range(k-1, -1, -1):
            # print(i)
            print(binary_representation[i])
            reversed_num += binary_representation[i]
        print(reversed_num)

        # convert a binary representation into a number:
        # print(int(binary_representation, 2))
        result_num = int(reversed_num, 2)
        print(result_num)
        return result_num

