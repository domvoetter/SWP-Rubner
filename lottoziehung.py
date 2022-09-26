import random

dict = {}

zahlen = []
for i in range(1, 46):
    zahlen.append(i)
    dict[i] = 0

for i in range(0, 1000):
    x = 0
    while x < 6:
        #rand = int(random.random() * (len(zahlen)-1-x) +1)
        rand = random.randrange(len(zahlen))
        zahlen[rand] = zahlen[len(zahlen)-1-x]
        zahlen[len(zahlen)-1-x] = rand
        dict[rand+1] += 1
        x += 1

#print(zahlen)
print(dict)