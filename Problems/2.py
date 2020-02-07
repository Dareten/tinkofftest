import timeit

m, s = int(input()), []
for _ in range(m - 1):
    s.append(int(input()))
a = timeit.default_timer()
t, i = True, 2
while t:
    for j in range(2, 2 + len(s)):
        if i % j != s[j - 2]:
            t = False
            break
    if t:
        print(i)
        t = False
        break
    t = True
    i += 2 - s[0]
print(timeit.default_timer() - a, end='')
