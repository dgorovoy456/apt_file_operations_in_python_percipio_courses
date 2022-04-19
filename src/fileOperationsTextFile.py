import os
import data_file
import subprocess

p = os.system('cat ../data_file/sample.txt')
print(p)

print(open('../data_file/sample.txt', 'r'))
file = open('../data_file/sample.txt', 'r')

print(file)
print(file.mode)
print(file.name)
print(file.closed)
file.close()
print(file.closed)

file = open('../data_file/sample.txt', 'r')

print(file.read())

print(file.seek(0))

print(file.read(5))

print(file.tell())

print(file.read(5))

print(file.tell())

