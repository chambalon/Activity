# Find sub string in a string

def find_string(s1,s2):

    count=0
    for i in range(len(s1)):
        if s1[i:len(s1)].startswith(s2):
            count+= 1
    print("occurance",count)
            
            
s1 = input()
s2 = input()

find_string(s1,s2)
