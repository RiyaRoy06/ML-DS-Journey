# Goal: Compare list.pop() vs list.pop(0).

def pop_from_start(list):
  target=list[0]
  N=len(list)
  for i in range(0,N-1):
    list[i]=list[i+1]
  list[N-1]=None
  return target
print(pop_from_start(list(range(1000))))
