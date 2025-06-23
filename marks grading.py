# Function to determine the grade based on marks
def determine_grade(marks):
    if marks > 90:
        return 'E'
    elif 80 <= marks <= 89:
        return 'A'
    elif 70 <= marks <= 79:
        return 'B'
    elif 60 <= marks <= 69:
        return 'C'
    elif 50 <= marks <= 59:
        return 'D'
    elif 35 <= marks <= 49:
        return 'P'
    else:
        return 'F'


# Taking input from the user
marks = float(input("Enter the marks of the student: "))

# Determining the grade and displaying the result
grade = determine_grade(marks)
print("The grade is:", grade)
