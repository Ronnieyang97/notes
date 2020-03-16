def solution():
    try:
        while True:
            line1 = input()
            line2 = input()
            length, tool = line1.split()
            length = int(length)
            tool = int(tool)
            list1 = [int(i) for i in line2.split()]
            count = {}
            for i in list1:
                if i in count.keys():
                    count[i] += 1
                else:
                    count.update({i: 1})
            result = max(count.values())
            target = 0
            for i, j in zip(count.items(), count.values()):
                if j == result:
                    target = i

            for i in list1:
                if i ^ tool == target[0]:
                    result += 1

            print(result)



    except:
        pass


solution()