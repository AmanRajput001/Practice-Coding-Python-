# Write a program to find the second largest number in an array.
def largest(array):
    maximum = -1
    for item in array:
        if maximum < item:
            maximum = item
    return maximum

def second_largest(array):
    maximum = largest(array)
    second_max = -1

    for item in array:
        if item > second_max and maximum is not item:
            second_max = item
    return second_max

# print(second_largest([4,5,6,7,1,2]))

#------------------------------------------------------------------------#

# Write a program to reverse an array in-place.
def reverse_array(array):
    start = 0
    end = len(array) - 1

    while(start < end):
        temp = array[start]
        array[start] = array[end]
        array[end] = temp

        start = start + 1
        end = end - 1
    return array

# print(reverse_array([1,2,3,4,5]))

#------------------------------------------------------------------------#

# Write a program to find duplicate values in an array of integers.
def find_duplicates(array):
    mapp = {}
    for item in array:
        mapp[item] = mapp.get(item, 0) + 1

    dup_array = []
    for item, value in mapp.items():
        if value > 1:
            dup_array.append(item)
    return dup_array

# print(find_duplicates([1, 1, 2, 3, 3, 3, 4, 5, 5]))

#------------------------------------------------------------------------#

# Write a program to count even and odd numbers in an array.
def count_odd_even(array):
    count_odd = 0
    count_even = 0

    for item in array:
        if item % 2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1
    return [count_even, count_odd]

# print(count_odd_even([1, 1, 2, 3, 3, 3, 4, 5, 5]))

#------------------------------------------------------------------------#

# Write a program to find common elements between two arrays.
def common_elements(array1, array2):
    common = []
    for item1 in array1:
        for item2 in array2:
            if item1 == item2:
                common.append(item1)
    return common

print(common_elements([1,2,3,4,5], [2,3,4,6,7]))