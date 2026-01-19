# Goal: Find index of number in sorted list.

def binary_search(arr,i):
  l,h=0,len(arr)-1
  while l<=h:
    m=(l+h)//2
    if arr[m]==i:
      return m
    elif arr[m]<i:
      l=m+1
    else: h=m-1
  return -1
print(binary_search([1,2,3,4,5],4))
