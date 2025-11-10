list1 = []
for i in range(int(input())):
  name = input()
  score = float(input())
  list1.append([name,score])
print(list1)
l2 = sorted(set([score for name,score in list1 ]))
print(l2)
sec_lowest_score = l2[1]
print(sec_lowest_score)
print(" ".join([name for name, score in list1 if score == sec_lowest_score]))