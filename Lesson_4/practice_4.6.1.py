from itertools import count, cycle

a = []
x = 0
for i in count(0):
    if i > 3:
        print(a)
        for el in cycle(a):
            if x > 8:
                break
            else:
                print(el)
                x += 1
        break
    else:
        print(i)
        a.append(i)
