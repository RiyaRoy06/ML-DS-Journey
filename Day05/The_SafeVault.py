# Goal: Create a dictionary user={"id":1}. Try to access user={"email"}. Then try to access it safely.

user={"id":1}
email=user.get("email","No email found")
print(email)
