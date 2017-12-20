a = range(3)
b = range(3)
print a
print b
c = []
for i in range(len(a)):
    a[i] = i ** 2
    b[i] = i ** 3
    c.append(a[i] + b[i])

print(c)
