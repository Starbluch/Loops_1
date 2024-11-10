# 1 Variant (all)
# number = abs(int(input("Enter a number: ")))
#
# null = 0
# suma = 0
# count = 0
#
# while number > 0:
#     suma += number % 10
#     if (number % 10) == 0:
#         null += 1
#     number //= 10
#     count += 1
# average = int(suma / count)
# print(f"suma: {suma} null: {null} count: {count} average: {average}")

# 2 Variant
def count_digits(number):
    count = 0
    while (number > 0):
        number //= 10
        count += 1
    return count

def suma_digits(number):
    suma = 0
    while (number > 0):
        suma += (number % 10)
        number //= 10
    return suma

def null_digits(number):
    null = 0
    while (number > 0):
        if (number % 10) == 0:
            null += 1
        number //= 10
    return null

def average_digit(number):
    suma = 0
    count = 0
    while (number > 0):
        suma += (number % 10)
        number //= 10
        count += 1
    return int(suma / count)

number = int(input("\nEnter a number to work with\n> "))
par = int(input("\nSelect the menu item (1-5)\n> "))
if (par == 1):
    print(f"\nCount {number}: {count_digits(number)}")
elif par == 2:
    print(f"\nSum {number}: {suma_digits(number)}")
elif par == 3:
    print(f"\nAverage {number}: {average_digit(number)}")
elif par == 4:
    print(f"\nNumber 0 {number}: {null_digits(number)}")
elif par == 5:
    print("\nGoodbye!")
    exit()
else:
    print("\nError!")