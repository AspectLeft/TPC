with open('exch_2.txt') as f:
    train = open('exch2.train.txt', 'w')
    valid = open('exch2.valid.txt', 'w')
    test = open('exch2.test.txt', 'w')

    for line in f:
        arr = line.split(' ')
        for i in range(len(arr)):
            if i < 0.8 * len(arr):
                train.write(arr[i])
                train.write(' ')
            else:
                valid.write(arr[i])
                valid.write(' ')
                test.write(arr[i])
                test.write(' ')
        train.write('\n')
        valid.write('\n')
        test.write('\n')
    train.close()
    valid.close()
    test.close()