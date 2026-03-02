import os

print(os.getcwd())

with open("logs.txt","r") as file:
    for line in file:
        if 'error' in line.lower():
            print(line)
        