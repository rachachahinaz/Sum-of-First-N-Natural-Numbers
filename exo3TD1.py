def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input("Enter a number: "))
sum = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {sum}")