a = int(input("Enter a number: "))
odd_numbers = [x for x in range(1, a + 1) if x % 2 != 0]
print(odd_numbers)