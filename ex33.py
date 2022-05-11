def no_0to10 (a):
    i = 0
    numbers = []

    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

no_0to10 (10)
