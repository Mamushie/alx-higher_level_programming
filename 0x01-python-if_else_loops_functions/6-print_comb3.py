#!/usr/bin/python3
for num in range(0, 10):
    for num1 in range(0, 10):
        if (num < num1):
            print("{}{}".format(num, num1), end="")
            if (num < 8):
                print(", ", end="")
print("\n", end="")
