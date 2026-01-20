# Goal: Write 1 million lines. Why doesn't the disk spin 1 million times.

with open('buf.txt','w') as f:
   [f.write(str(i)+'\n') for i in range(1000000)]
print(f.closed)
