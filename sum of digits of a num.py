num = int(input("Enter a number: "))
result = 0
while num != 0:
    temp = num % 10
    result = result + temp
    num = num // 10
print("The sum of the digits is ", result)
