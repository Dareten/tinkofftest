import timeit
c = 0
x, y = [int(i) for i in input().split()]
a = timeit.default_timer()
while x < y:
    x, c = x * 1.7, c + 1
print(timeit.default_timer() - a)
print(c)
