with open('tpc_c.disksim') as f:
    a = 0
    count = 0
    address = 0
    for line in f:
        arr = line.split(' ')
        if a < int(arr[1]):
            a = int(arr[1])
        if address < int(arr[2]):
            address = int(arr[2])
        count += 1
    print(a)
    print(address)
    print(count)
