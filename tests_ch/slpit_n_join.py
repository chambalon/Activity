def split_and_join(s):

    s_list = s.split()
    print(s_list)
    string = "-".join(s_list)

    return string

#s="python is awesome"
s=input() 
op=split_and_join(s)
print(op)