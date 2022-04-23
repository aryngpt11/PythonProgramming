#Python program to convert all units of time into seconds

days = int(input("enter days: ")) * 3600 * 24
hours = int(input("enter hours: ")) * 3600
minutes = int(input("enter minutes: ")) * 60
seconds = int(input("enter seconds: "))
time = days + hours + minutes + seconds
print("The  amounts of seconds= ", time)
