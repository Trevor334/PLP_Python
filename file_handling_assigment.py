file = open('my_file.txt', 'w')
file.write('New text file\n')
file.write(str(7))
file.write(' is the number of completion\n')
file.close()
file_read = open('my_file.txt', 'r')
print(file_read.read())
file.close()
file_append = open('my_file.txt', 'a')
file_append.write('Content added to file\n')
file_append.write('without truncation\n')
file_append.write('Very very nice\n')
file_append.close()
file_append_read = open('my_file.txt', 'r')
print(file_append_read.read())
file_append_read.close()