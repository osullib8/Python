for i in range (1, 100):
    prime = False

    for n in range (2, i-1):
        if (i % n == 0):
            prime = True
            break

    if (prime == False):
        print(i, "is a Prime number")
    