# Goal: Slice a massive list data[0:1000].

def slice_list(source,k):
    # Step 1: Allocate memory for k items
    new_list=[None]*k
    # Step 2: Copy values one by one
    for i in range(k):
        new_list[i]=source[i]   # copy reference
    return new_list
data=list(range(1000000))
result=slice_list(data,100)
print(result)
