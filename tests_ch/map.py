
# find the length of eac element in a tuple
mytuple = ("Blue","Violet","red")

def length(n):
    return len(n)

x= map(length,mytuple)
print(x)
print(list(x))

print("******************************")

# Combine the elements of two tuples
mytuple2 = ("sky","flower","ribbon")

def myfunc(first,second):
    return first+second

y = map(myfunc,mytuple,mytuple2)
print(list(y))
print("******************************")

mytuple = ("Blue","Violet","red")
x=map(lambda a:len(a),mytuple)
print(list(x))
print("******************************")

mytuple2 = ("sky","flower","ribbon")
y = map(lambda a,b: a+b,mytuple,mytuple2)
print(list(y))