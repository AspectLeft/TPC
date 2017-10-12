with open('E:/trace/SPC traces/Financial1.spc') as f:
    out = open('spc.disksim', 'w')
    for line in f:

        arr = line.split(',')


        out.write(str(float(arr[4]) * 1000.0))  # second -> millisecond
        out.write(' ')
        out.write(arr[0])  # ASU -> devNum
        out.write(' ')
        out.write(arr[1])  # blockNum, the size of a block is 512
        out.write(' ')
        out.write(str(int(int(arr[2]) / 512)))  # size in bytes
        out.write(' ')
        if arr[3] == 'w':
            out.write('0')
        else:
            out.write('1')
        out.write('\n')
    out.close()
