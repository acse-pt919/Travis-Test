
N = 20
test = 2
primes = []
while len(primes)<N:
    for p in primes:
        if p**2>test:
            primes.append(test)
            break
        if test%p==0:
            break
    # special case
    if len(primes)==0:
        primes.append(test)
    test += 1
print(primes)