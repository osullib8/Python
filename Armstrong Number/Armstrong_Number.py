for n in range(0, 1000):
    str_n = str(n)
    len_n = len(str_n)
    sum_n = 0

    for x in str_n:
        sum_n += int(x) ** len_n

    if (sum_n == n):
        print(n ," is an Armstrong number")