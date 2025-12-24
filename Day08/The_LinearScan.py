# Goal: Create a list of 10 million numbers. Check if -5 is in the list.

def contains(list,target):
    index=0
    length=len(list)
    while index<length:
        current_value=list[index]
        if current_value==target:
            return True
        index=index+1
    return False
print(contains(list(range(1000001)),-5))
