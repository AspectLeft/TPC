import csv

with open('E:/trace/Microsoft Production Server Traces/BuildServer00/BuildServer/Traces/24.hour.BuildServer.11-28-2007.07-24-PM.trace.csv') as f:
    f_csv = csv.reader(f)
    out = open('out.disksim', 'w')
    i = 0
    count = 0
    max = 0
    for row in f_csv:
        i += 1
        if i > 70:
            if row[0] == '               DiskRead' or row[0] == '              DiskWrite':
                out.write(str(float(row[1]) / 1000.0))  # timestamp, microseconds -> milliseconds
                out.write(' ')
                out.write(row[8].strip())  # device number
                out.write(' ')
                out.write(str(int(int(row[5], 0) / 256))) # block number, blocking factor == 256
                out.write(' ')
                out.write(str(int(int(row[6], 0) / 256))) # size in blocks
                out.write(' ')
                if row[0] == '               DiskRead':
                    out.write('1')
                else:
                    out.write('0')

                out.write('\n')
    out.close()