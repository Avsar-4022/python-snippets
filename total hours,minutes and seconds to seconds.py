hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
hours_to_seconds = hours*3600
minutes_to_seconds = minutes*60
total_seconds = hours_to_seconds + minutes_to_seconds + seconds
print(f"The total number of seconds is {total_seconds} ")
