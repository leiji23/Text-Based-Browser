# read test_file.txt
file = open('test_file.txt', 'r', encoding='utf-16')
first_line = file.readline()
print(first_line)
file.close()
