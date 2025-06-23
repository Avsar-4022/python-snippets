def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI).

    Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.

    Returns:
        float: BMI value.
    """
    bmi = weight / (height ** 2)
    return bmi


def classify_bmi(bmi):
    """
    Classifies BMI into categories.

    Args:
        bmi (float): BMI value.

    Returns:
        str: BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def main():
    try:
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))

        bmi_value = calculate_bmi(weight, height)
        bmi_category = classify_bmi(bmi_value)

        print(f"Your BMI is {bmi_value:.2f} ({bmi_category})")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for weight and height.")


if __name__ == "__main__":
    main()
