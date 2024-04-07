with open("tanggal.txt") as fp:
    count = 0
    for line in fp:
        count += 1
        print(line.strip())