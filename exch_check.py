with open('exch.disksim') as f:
    stride = 1
    i = 0
    maxBlock = 0
    sizes = set()
    blkPerDev = {}
    tracePerDev = {}
    minT = 100000.0
    maxT = 0.0
    for line in f:
        i += 1
        if i == stride:
            i = 0
            arr = line.split(' ')
            blkNum = int(arr[2])
            devNum = int(arr[1])
            t = float(arr[0])
            if t < minT:
                minT = t
            if t > maxT:
                maxT = t
            if devNum in blkPerDev:
                if blkPerDev[devNum] < blkNum:
                    blkPerDev[devNum] = blkNum
            else:
                blkPerDev[devNum] = blkNum
            if devNum in tracePerDev:
                tracePerDev[devNum] += 1
            else:
                tracePerDev[devNum] = 1
            size = int(arr[3])
            sizes.add(size)
            # print(blkNum)
            if blkNum > maxBlock:
                maxBlock = blkNum

    print(blkPerDev)
    print(maxBlock)
    print(sizes)
    print(tracePerDev)
    print(minT)
    print(maxT)