# Goal: Convert that list to a set. Check for -5 again.

def set_contains(hash_set,target):
    # Step 1: Compute mathematical signature
    hash_value=hash(target)
    # Step 2: Calculate memory address
    bucket_index=hash_value % len(hash_set)
    # Step 3: Direct Jump
    memory_slot=hash_set[bucket_index]
    if target in memory_slot:
        return True
    else:
        return False
hash_set=[[] for _ in range(10)]
for i in range(100):
    idx=hash(i) % len(hash_set)
    hash_set[idx].append(i)
print(set_contains(hash_set,-5))
