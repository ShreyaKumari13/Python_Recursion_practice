'''
    3. Write a Python program of recursion list sum.
    Test Data: [1, 2, [3,4], [5,6]]
    Expected Result: 21
'''
def sum_list(list1):
    sum1 = 0
    sum2 = 0
    for i in list1:
        if type(i)==list:
            for j in i:
                sum1+=j
        else:
            sum2+=i
    return sum1,sum2
list1 = [1, 2, [3,4], [5,6]]
print(sum_list(list1))

def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))

