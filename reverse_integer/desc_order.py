
'''Your task is to make a function that can take any non-negative integer 
as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
Examples:

Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321'''

def descending_order(num):
    # Bust a move right here
    # shortest solution:
    return int(''.join((sorted(str(num))[::-1])))

    ##came up with the below, also works btw:
    # ls_num = [i for i in str(num)]
    # ls_num.sort(reverse=True)
    # print(ls_num)
    # str_num = ''.join(ls_num)
    # int_num = int(str_num)
    # return int_num


print(descending_order(1201))