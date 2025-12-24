# Goal: Measure the time to create a dict from a list vs searching it.

def build_dict_from_list(list):
    new_dict=allocate_memory(list)
    for item in list:
        hash_val=calculate_hash(item,len(new_dict))
        slot=find_empty_slot(hash_val)
        new_dict[slot]=item
    return new_dict
def allocate_memory(list):
    return [None]*len(list)
def calculate_hash(item,size):
    return hash(item) % size
def find_empty_slot(hash_val):
    return hash_val   # no collision handling (conceptual)
data=list(range(1_000_000))
start=time.time()
hash_table=build_dict_from_list(data)
end=time.time()
print("Time to create dict:",end-start)
start=time.time()
end = time.time()
print("Time to search in list:",end-start)
