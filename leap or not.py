num = int(input("Enter the year: "))
if (num % 4 == 0) and (num % 100 != 0) or (num % 400 == 0):
    print("year is leap")
else:
    print("year is not leap")
