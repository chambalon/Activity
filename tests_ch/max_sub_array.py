# Find sum of array elements

def max_sub_array(arr):

    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum+arr[i])
        max_sum = max(arr[i], current_sum)

    return max_sum


sum = max_sub_array([1,2,3])
print(sum)