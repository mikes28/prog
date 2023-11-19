asked_count = int(input("Enter the count of numbers:"))
count = 0
curr_number = 1

while count < asked_count:
    divisible = True
    for i in range(2, 10):
        if curr_number % i != 0:
            divisible = False
            break
    if divisible:
        count += 1
        print(curr_number)
    curr_number += 1

