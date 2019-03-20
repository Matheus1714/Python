cache = {}
def threen(n):
    if n in cache:
        return cache[n]
    if n ==1:
        return 1
    orig = n
    if n%2 == 0:
        n = n/2
    else:
        n = 3*n+1
    count = threen(n)+1
    cache[orig] = count
    return count
def max_threen(i, j):
    max3n = 0
    for n in xrange(i, j+1):
        max3n= max(threen(n), max3n)
    print i, j, max3n
max_threen(100,201)
max_threen(900,1000)