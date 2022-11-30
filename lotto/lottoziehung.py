import random

dict = {}

zahlen = []

def ziehung_range(min, max):
    for i in range(min, max+1):
        zahlen.append(i)
        dict[i] = 0

def ziehung(anz):
    for i in range(anz):
        index = random.randrange(len(zahlen))
        value = zahlen[index]
        zahlen[index] = zahlen[len(zahlen)-1-i]
        zahlen[len(zahlen)-1-i] = value
        statistik(index)
        i += 1

def statistik(x):
    dict[x+1] +=1

if __name__ == "__main__":
    ziehung_range(1, 10)
    for i in range(0, 1000):
        #print(zahlen)
        ziehung(6)
    print(dict)