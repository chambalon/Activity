n = int(input())
a1 = list(map(int, input().split()))
#Remove duplicates
a2 = set(a1)
a3 = sorted(a2)
print(a3[-2])