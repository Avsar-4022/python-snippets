def get_age_group(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif 20 <= age <= 59:
        return "Adult"
    else:
        return "Senior Citizen"


def main():
    try:
        age = int(input("Enter your age: "))
        age_group = get_age_group(age)
        print(f"You belong to the age group: {age_group}")
    except ValueError:
        print("Invalid input. Please enter a valid age as a positive integer.")


if __name__ == "__main__":
    main()
