file = open('../data_file/sample.txt', 'r')

print(file.read())
print(file.seek(0))
print(file.read(5))
print(file.tell())

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

file.seek(0)

print('##################################################')

print(file.readlines())

file.close()
print(file.closed)

with open('../data_file/sample.txt') as f:
    data = f.readlines()
print(data)

print(file.closed)

print('####################################################')

with open('../data_file/sample.txt') as f:
    line = f.readline()

    while line:
        print(line)
        line = f.readline()

print(file.closed)

