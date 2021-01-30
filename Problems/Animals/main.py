# read animals.txt
file = open('animals.txt', 'r')
file_to_write = open('animals_new.txt', 'w')
new_text = []
for line in file:
    new_text.append(line.replace('\n', ' '))
file_to_write.writelines(new_text)
file.close()
file_to_write.close()
