# Goal: Create a new list numbers from 1 to 10. Generate a new list containing the squares of only the even numbers.

data=[1,2,3,4,5,6,7,8,9,10]
new_data=[x**2 for x in data if x%2==0]
print("new list: ",new_data)
