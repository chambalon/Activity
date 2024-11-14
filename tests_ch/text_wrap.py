import textwrap

def wrapText(s,w):

    return textwrap.fill(s,w)


s= input()
w= int(input())

op = wrapText(s,w)
print(op)