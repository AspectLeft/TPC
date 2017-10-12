with open('exch.disksim') as f:
    stride = 262144  # in blocks
    period = 9000  # ms
    out = open('exch_2.txt', 'w')

    maxBlock = 2143289344
    maxT = 905000

    table = []
    for i in range(maxBlock // stride + 1):
        table.append([0] * (maxT // period + 1))


    for line in f:
        arr = line.split(' ')
        if arr[1] == '2':
            t = float(arr[0])
            blkNum = int(arr[2])
            size = int(arr[3])
            zoneNum = blkNum // stride
            table[zoneNum][int(t / period)] += 1
            blkNum += size
            if blkNum // stride > zoneNum:
                table[zoneNum + 1][int(t / period)] += 1
    for line in table:
        for i in line:
            out.write(str(i))
            out.write(' ')
        out.write('\n')
    out.close()

