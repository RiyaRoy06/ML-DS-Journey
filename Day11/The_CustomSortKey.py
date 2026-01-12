# Goal: Sort["100px","20px","3px"] numerically(so 3px comes first).

result=sorted(["100px","20px","3px"] ,key=lambda x:int(x[:-2]))
print("The result is: ",result)
