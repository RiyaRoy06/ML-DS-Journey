# Goal: Find duplicates between two lists using nested for loops.

def find_duplicates(list1,list2):
  matches=[]
  for item1 in list1:
    for item2 in list2:
      if item1==item2:
        matches.append(item1)
  return matches
print("Duplicate Values are:",find_duplicates([1,2,3,4,5],[3,4,5,6,7]))
