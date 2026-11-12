def is_armstrong(num):
    if num < 0:
        return False
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num

# Example usage
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
