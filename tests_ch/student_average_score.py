
dict = {}
for i in range(int(input("n: "))):
  # Unpacking assignment
  # First element of split list is assigned to name and a new list of all remaining elements is assigned to scores.
  name, *scores = input("name & marks: ").split()
  scores_list = list(map(float,scores))
  dict[name] = scores_list
print(dict)
query_name = input("name: ")
student_scores = dict[query_name]
avg = sum(student_scores)/len(student_scores)
print(avg)