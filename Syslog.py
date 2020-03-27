with open(r'C:\Users\Max\CPSC\evtx\log.txt') as data:
    header = data.read(24)
    text = data.read().decode('utf-16-le')
