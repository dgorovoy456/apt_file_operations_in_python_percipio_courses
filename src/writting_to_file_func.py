import os

file = open('../data_file/example.txt', 'w')  # using when we just
file.close()  # need to reate a new file

file = open('../data_file/example.txt', 'w')
file.write('Let`s check the write operation')
file.close()
print(os.system(f'cat ../data_file/example.txt'))
print(file.closed)

print('###########################################')

file = open('../data_file/example.txt', 'w')
file.write('Let`s check the write operation')
file.seek(6)
file.write(' examine ')
file.close()
print(os.system(f'cat ../data_file/example.txt'))

print('#########################################')

file = open('../data_file/example.txt', 'r')
for lines in file:
    print(lines)
print(file.closed)
file.close()
print(file.closed)

print('#########################################')

with open('../data_file/example.txt', 'w') as f:
    f.write('First line\n')
    f.write('Second line\n')
    f.write('Third line\n')
print(os.system('cat ../data_file/example.txt'))

print('##########################################')

with open('../data_file/example.txt', 'a') as f:
    f.write('First line\n')
    f.write('Second line\n')
    f.write('Third line\n')
print(os.system('cat ../data_file/example.txt'))

print('#############################################')

with open('../data_file/example.txt', 'a') as f:
    f.writelines(['Another line\n',
                  'Whet it will look like now\n',
                  'Let`s check it out\n'])

with open('../data_file/example.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()

print('#########################################')

f = open('../data_file/example.txt')
print(f.fileno())
print(f.isatty())
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)


print('###############################')

f = open('../data_file/example.txt', 'a')
print(f.tell())

size = os.stat('../data_file/example.txt').st_size
print(size)

f.close()

print('#############################################')

f = open('../data_file/example.txt', 'a')
f.truncate(37)
f.close()

f = open('../data_file/example.txt', 'r')
print(f.read())
f.close()

f = open('../data_file/example.txt', 'r+')
f.writelines("We are doing an 'r+' operation")
f.close()

f = open('../data_file/example.txt', 'r')
print(f.read())
f.close()

print('###############################################')

f = open('../data_file/example.txt', 'a+')
f.writelines('\nWhat does writing in "a+" do?')
f.close()

f = open('../data_file/example.txt', 'r')
print(f.read())
f.close()

os.rename('../data_file/example.txt', '../data_file/changed_name.txt')
# os.remove('../data_file/changed_name.txt')

