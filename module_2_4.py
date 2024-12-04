numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_not_prime = True
for i in numbers:
    for j in range(2, len(numbers)):
        if i % j != 0:
            is_not_prime = False
            continue
        elif i != j and i % j == 0:
            is_not_prime = True

        if is_not_prime:
            not_primes.append(i)
            break
        else:
            primes.append(i)
            break
print(primes)
print(not_primes)
