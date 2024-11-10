#lessons 1.1 hm
def prime_numbers():
    start = int(input("Enter the start value: "))
    finish = int(input("Enter the finish value: "))

    print(f"Prime numbers in the range from {start} to {finish}:")
    for i in range(start, finish + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)
