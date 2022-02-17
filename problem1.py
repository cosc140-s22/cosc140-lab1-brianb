#
# Name: Brian
# Collaborator(s): None :(   
# 

seconds = input("How many seconds? ")
seconds = int(seconds)
secondsS = seconds%(3600*24)%60

minutes = seconds%(3600*24)//60%60

hours = seconds%86400//3600

days = seconds//86400

print("minutes:",minutes)
print("days",days)
print("hours",hours)
print("seconds",secondsS)



