def print_rhombus(size):
    for i in range(1, size + 1):
        print(' ' * (size - i) + '*' * (2 * i - 1))

    for i in range(size - 1, 0, -1):
        print(' ' * (size - i) + '*' * (2 * i - 1))


size = int(input("Enter size rhombus: "))

print_rhombus(size)