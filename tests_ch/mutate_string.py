# Add a character at a given position
def mutate_string(s,i,c):
    s_list = list(s)
    s_list[i] = c
    #print(s_list)
    updated_s = "".join(s_list)
    return updated_s

s= input()
i,c = input().split()
op= mutate_string(s,int(i),c)
print(op)