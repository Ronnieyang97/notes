i = 2
while (100/i - i/2) >= 1:
    i += 1

for n in range(2, i):
    if 100/n % 1 == 0 and n % 2 == 1:
        if sum(range(int(100/n - n/2 + 1), int(100/n + n/2 + 1))) == 100:
            print(list(i for i in range(int(100/n - n/2 + 1), int(100/n + n/2 + 1))))

    if 100/n % 1 == 0.5 and n % 2 == 0:
        if sum(range(int(100/n - n/2 + 1), int(100/n + n/2 + 1))) == 100:
            print(list(i for i in range(int(100/n - n/2 + 1), int(100/n + n/2 + 1))))



