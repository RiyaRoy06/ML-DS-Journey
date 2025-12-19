# Goal: Create a list of 1 million numbers. Create a set(hash table) of the same numbers. Check if the number -1 exists in both.

List=list(range(1000001))
Set=set(List)
print(-1 in List)
print(-1 in Set)
#explanation in Day05.md
