# map() to convert a list of strings into a list of integers.

ls = ['1','2','3']
output = map(int,ls)
#print(output)
li = list(output)
print((li))

print("*********************************")

a = [1,2,3,4,5]

def power(num):
    return num**2

output = map(power,a)

a_updated = list(output)
print(a_updated)

print("*********************************")

x = [1,2,3,4]

output = map(lambda a: a*3, x)
x_updated = list(output)
print(x_updated)