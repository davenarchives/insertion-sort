list = []

def userInput(): # user-input 
    n = int(input("Enter number of elements: "))

    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        list.append(num)

def insertionSortAscend(list, n): # function for insertion sort in ascending order

    for i in range(0, n):
        keys = list[i]
        j = i - 1
        while j >= 0 and list[j] > keys:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = keys
    return list

def insertionSortDescend(list, n): # function for insertion sort in descending order


    for i in range(0, n):
        keys = list[i]
        j = i - 1
        while j >= 0 and list[j] < keys:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = keys
    return list

userInput()
list1 = insertionSortAscend(list, len(list))
print(f"Ascending Order: {list}")
list2 = insertionSortDescend(list, len(list))
print(f"Descending Order: {list}")

