# Goal: Compare list.appened(x) vs list.insert(0,x)

def insert_at_zero(list,new_value):
    N=len(list)
    list.append(None)
    for i in range(N,0,-1):
        list[i]=list[i-1]
    list[0]=new_value
data1=list(range(1000000))
data2=list(range(1000000))
start=time.time()
data1.append(99)
end=time.time()
print("Time for append:",end-start)
start=time.time()
insert_at_zero(data2,99)
end=time.time()
print("Time for insert at index 0:",end-start)
