import csv

file = open('../data_file/record.csv', 'r')

with file:
    read = csv.reader(file)

    for row in read:
        print(row)

file = open('../data_file/record_pipe.csv', 'r')

with file:
    read = csv.reader(file)

    for row in read:
        print(row)

print('############################################################\n')

file = open('../data_file/record.csv', 'r')

with file:
    read = csv.reader(file, delimiter='|')

    for row in read:
        print(row)

print('#############################################################\n')

file = open('../data_file/record_pipe.csv', 'r')

with file:
    read = csv.reader(file, delimiter='|')

    for row in read:
        print(row)

print('###############################################################\n')


file = open('../data_file/record_tab.csv', 'r')

with file:
    read = csv.reader(file)

    for row in read:
        print(row)

print('###############################################################\n')


file = open('../data_file/record_tab.csv', 'r')

with file:
    read = csv.reader(file, delimiter="\t")

    for row in read:
        print(row)

print('###############################################################\n')
print('###############################################################\n')

file = open('../data_file/record.csv', 'r')

with file:
    read = csv.DictReader(file)

    for row in read:
        print(row)
        print(dict(row))

print('###############################################################\n')

names = [['FirstName', 'Last Name'],
         ['Sofia', 'Reyes'],
         ['Jerome', 'Jackson'],
         ['Jia', 'Zhong']]


file = open('../data_file/names.csv', 'w')

with file:
    file_writer = csv.writer(file)

    for row in names:
        file_writer.writerow(row)


print('#############################################################')
print('#############################################################\n')

file = open('../data_file/names.csv', 'w')

with file:

    fnames = ['FirstName', 'LastName']
    writer = csv.DictWriter(file, fieldnames=fnames)

    writer.writeheader()
    writer.writerow({'FirstName': 'Sofia', 'LastName': 'Reyes'})
    writer.writerow({'FirstName': 'Jerome', 'LastName': 'Jackson'})
    writer.writerow({'FirstName': 'Jia', 'LastName': 'Zhong'})




