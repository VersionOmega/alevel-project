import anytree, string
number = 11
tempList = []
alpha = ["", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

count = 0

for i in range(number**2 + 1):
    a = count//(26**3)
    b = count//(26**2)
    c = count//(26**1)
    d = count//(26**0)+1

    temp = (count - c*26)+1
    count += 1
    tempList.append(f"{alpha[a]}{alpha[b]}{alpha[c]}{alpha[temp]}")

print(tempList)


def printArray(array):
    for line in array:
        print(line)

number = 5

array = [[] for i in range(number)]
for column in array:
    for i in range(number):
        column.append("*")

index = (0,0)
direction = (0, 1)
indexList = []
for i in range(number**2):
    array[index[0]][index[1]] = i
    indexList.append(index)

    temp = ((index[0]+direction[0]), (index[1]+direction[1]))
    
    if direction == (0, 1) and temp[1] <= number-1 and temp not in indexList:
        index = temp
    elif direction == (0, 1) and temp[1] > number-1:
        direction = (1, 0)
        index = ((index[0]+direction[0]), (index[1]+direction[1]))
    
    elif direction == (1, 0) and temp[0] <= number-1 and temp not in indexList:
        index = temp
    elif direction == (1, 0) and temp[0] > number-1:
        direction = (0, -1)
        index = ((index[0]+direction[0]), (index[1]+direction[1]))

    elif direction == (0, -1) and temp[1] >= 0 and temp not in indexList:
        index = temp
    elif direction == (0, -1) and temp[1] < 0:
        direction = (-1, 0)
        index = ((index[0]+direction[0]), (index[1]+direction[1]))

    elif direction == (-1, 0) and temp[0] >= 0 and temp not in indexList:
        index = temp
    elif direction == (-1, 0) and temp[0] < 0:
        direction = (0, 1)
        index = ((index[0]+direction[0]), (index[1]+direction[1]))
    
    print("\n\n")
    printArray(array)



#printArray(array)