def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



for i in range(100):
    if is_prime(i) == True:
        print(i)


