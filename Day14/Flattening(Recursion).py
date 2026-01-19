# Goal: Flatten [1,[2,[3,4]]] into [1,2,3,4].

def flat(r):
  a=[]
  for i in r:
    if isinstance(i,list):
      a+=flat(i)
    else:
      a.append(i)
  return a
print(flat([1,[2,[3,4]]]))
