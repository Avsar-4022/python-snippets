# Prompt the user to input a number from 1 to 7
day_number = int(input("Enter a number from 1 to 7: "))

# Dictionary to map numbers to days
days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

# Display the corresponding day
if 1 <= day_number <= 7:
    print(f"The day is {days[day_number]}")
else:
    print("Please enter a number between 1 and 7.")
