# read sums.txt
file = open('sums.txt', 'r')
for line in file:
    print(int(line.split(' ')[0]) + int(line.split(' ')[1]))
file.close()
