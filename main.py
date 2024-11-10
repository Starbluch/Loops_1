#lessons 1.3 hm

def calculator():
    start=int(input("Enter the start value: "))
    finish=int(input("Enter the finish value: "))

    for start in range (start, finish+1):
        print()
        for i in range (1,11):
            print(f"{start} * {i} = {start * i}{" |"}", end=" ")
