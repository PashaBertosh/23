def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

count = 0
num = 2

while True:
    if is_prime(num):
        count += 1
        if count == 1001:
            print(f"The 1001-st prime number is: {num}")
            break
    num += 1
