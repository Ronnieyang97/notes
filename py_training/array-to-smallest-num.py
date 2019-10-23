test = [321, 32, 3]

for i in range(len(test)):
    test[i] = str(test[i])
for i in range(1, len(test)):
    if (test[i-1] + test[i]) > (test[i] + test[i-1]):
        test[i-1], test[i] = test[i], test[i-1]
    else:
        continue
print(''.join(test))
