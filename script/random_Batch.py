import random
count = 1
m = 1000
result = [None] * m
sl = (230, 110, 50, 50, 60, 50, 30, 10, 20, 150, 100)

# 140,230,110,50,50,60,50,30,10,20,150,100

l = set(range(m))
x = set(random.sample(l, 140))
for i in x:
    result[i] = count


for j in sl:
    print(j)
    count += 1
    l = l - x
    x = set(random.sample(l, j))
    for i in x:
        result[i] = count


for i in result:
    print(i)
