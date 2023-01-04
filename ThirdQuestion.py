def SortArray(text: str):
    text = text.replace("[", "")
    text = text.replace("]", "")
    array = text.split(",")
    for i in range(len(array)):
        array[i] = int(array[i])
    numbers = array
    swapsCount = 0
    for i in range(len(numbers)):
        while numbers[i] != i + 1:
            temp = numbers[i]
            numbers[i] = numbers[numbers[i] - 1]
            numbers[temp - 1] = temp
            swapsCount += 1
    print(swapsCount)


userArray = input()
SortArray(userArray)
