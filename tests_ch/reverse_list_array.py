def reverse_array(arr):
    reverse_arr= []
    max_indx= n-1
    for i in range(n):
        reverse_arr.append(arr[max_indx-i])
    return reverse_arr
   

n=int(input("Enter the array length ( integer between 1 to 10):"))
arr=input("enter array numbers:").split()
output= reverse_array(arr)
print(*output)
