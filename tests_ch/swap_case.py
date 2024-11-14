
def swapcase(s):

    swaped_s = ""

    for i in s:
        if i.isupper() == True:
            i = i.lower()
            swaped_s+= i
        else:
            i=i.upper()
            swaped_s+= i

    return swaped_s


s = " PythoN Is aWeSomE"
op= swapcase(s)
print(op)