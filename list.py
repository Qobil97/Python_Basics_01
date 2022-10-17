names=['john', 'boob', 'moosh', 'sarah', 'kakau']
names[0]='jon'
print(names[:])
print(names)


#max number in the list
numbers=[3,6,7,8,4,14]
max=numbers[0]

for number in numbers:
    if number > max:
        max=number
print(max)
