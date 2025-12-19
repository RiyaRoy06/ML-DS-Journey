# Goal: Input a string "banana". Create a dictionary that counts the frequency of each letter(e.g., {'b':1,'a':3,'n':2}).

string="banana"
freq={}
for ch in string:
  if ch in freq:
    freq[ch]=freq[ch]+1
  else:
    freq[ch]=1
print(freq)
