mylist = ["I","am",100]
mytuple = ("row","row","row your boat",101)

mystringlist = ["hi","hello"]

print(mylist)
print(mytuple)

# Unpack operator
print(*(mylist))
print(*(mytuple))

print(*(mylist), sep="->")
print(*(mytuple), sep="/")

#join operator for string list
print("".join(mystringlist))

for e in mylist:
    print(e)

for e in mytuple:
    print(e)

# End operator removes newline character
for e in mylist:
    print(e, end=" ")
print("\n")
for e in mytuple:
   print(e, end="/")
