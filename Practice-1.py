def solve(n, m, a):
    remainder = 0
    for i in a:
        remainder = (remainder + i) % m
    print('remainder: ' + str(remainder))

solve(5,7,(1,2,3,4,5))
### remainder: 1
