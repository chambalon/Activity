
"""num = int(input("Enter an integer:"))

def print_num_decrease(num):    
    while num > 0:
        print(num)
        print_num_decrease(num-1)
        break
print_num_decrease(num)

print("*******************************")"""


num = int(input("Enter an integer:"))

def print_num_decrease(num):    
    if num == 0:
        # Terminate the function without returning any value
        return
    #else:
    print(num)
    print_num_decrease(num-1)
        
print_num_decrease(num)
