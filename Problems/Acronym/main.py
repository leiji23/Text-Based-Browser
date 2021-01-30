# read test.txt
file = open('test.txt', 'rt')
for line in file:
    # if line != '\r\n' and line != '\n' and line != '\r':
    print(line[0])
file.close()
