# Goal: Loop thrpugh numbers 1 to 10.  But if the number is 5, skip it and do not print anything.

i=1
while i<=10:
  if i==5:
    i+=1
    continue
  print(i)
  i+=1
