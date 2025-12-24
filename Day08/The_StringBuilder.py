# Goal: Loop 10000 times and add a character to a string using s+="a".

def add_char(old_string,char):
    old_size=len(old_string)
    new_size=old_size+1
    # Step 1: Allocate New memory block
    new_memory=['']*new_size
    # Step 2: Copy ALL characters from old to new
    for i in range(old_size):
        new_memory[i]=old_string[i]
    # Step 3: Add the new character
    new_memory[old_size]=char
    # Step 4: Return new string
    return ''.join(new_memory)
print(add_char("How are you",'?')) 
