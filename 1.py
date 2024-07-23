'''
    1. Write a Python program to calculate the sum of a list of numbers.
'''
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])
        
print(list_sum([2, 4, 5, 6, 7]))

def sum_list(list1):
    sum1 = 0
    for i in list1:
        sum1+=i
    return sum1
list1 = [1,2,3]
print(sum_list(list1))

    