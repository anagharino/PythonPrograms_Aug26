n = int(input("Enter a number: "))

temp = n
digits = len(str(n))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    digits = digits - 1
    temp = temp // 10

if sum == n:
    print("Disarium Number")
else:
    print("Not a Disarium Number")