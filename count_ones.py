#Count how many 1 in binary representation of a 32-bit integer.
class Solution:
    """
    @param num: An integer
    @return: An integer, the number of ones in num
    """
    def count_ones(self, num: int) -> int:
        # write your code here
        #binary_representation = format(int('-1'), '032b')
        if not num:
            return 0
        result = 0
        binary_representation = format(num, '032b')
        print(binary_representation)
        input_num = int(binary_representation) # this removes leading zero and convert it into integer. 
        print(input_num)
        # exit()
        while input_num:
            # input_num = int(binary_representation)
            result += input_num % 2
            print(result)
            binary_input = binary_representation[:-1]
            # binary_input = binary_input >> 1 #Returns n with the bits shifted to the left by 1 places in binary representation
            # print("binary_input", binary_input)
            # exit()
            if binary_input: 
                input_num = int(binary_input)
            # exit()

        # print(result)
        return result

        exit()
        result = 0
        binary_num = bin(num) # note: bin() gives a binary represenation in str. 
        if num >= 0:
            binary_input = binary_num[2:] # this is not integer, could use slice
        else:
            # binary_num.replace('-', "")
            binary_input = binary_num[3:] # this is not integer, could use slice
            print(binary_num, binary_input)
        # exit()
        # print(binary_num[2:], type(binary_num[2:])) # slicing in python [left +1, right +1]
        # binary_input = binary_num[2:] # this is not integer, could use slice
        input_num = int(binary_input)
        
        for i in range(len(binary_input)):
            input_num = int(binary_input)
            result += input_num % 2
            print(result)
            binary_input = binary_input[:-1]
            # binary_input = binary_input >> 1 #Returns n with the bits shifted to the left by 1 places in binary representation
            print(binary_input)
            if binary_input: 
                input_num = int(binary_input)
            # exit()

        # print(result)
        return result
        

        


        
