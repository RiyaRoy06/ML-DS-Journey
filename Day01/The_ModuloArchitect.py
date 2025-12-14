# Goal: Input a row number of seconds(e.g.,3665). Use Integer Division // and Modulo % to calculate exactly how many Hours,Minutes and Seconds this represent.

sec=int(input("Enter number of seconds:"))
hours=sec//3600

minutes=(sec%3600)//60
seconds=sec%60
print(f"Hours:{hours} ; Minutes:{minutes} ; Seconds:{seconds}")
