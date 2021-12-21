for i in range (1, 100):
    sum = 0
    
    for n in range (1, i):
        if (i % n == 0):
            sum = sum + n
            
    if (sum == i) :
        print(i, "is a perfect number ")