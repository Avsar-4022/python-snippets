num = int(input("Enter a number: "))
new_num = 0
while (num != 0) :
    temp = num % 10
    new_num = new_num * 10 + temp
    num = num // 10
2025
print(f"the number after reversing is {new_num}")
