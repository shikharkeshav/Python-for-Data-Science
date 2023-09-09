def selectionSort(list1):
    size=len(list1)
    for index in range(size):
        min_index = index
 
        for j in range(index + 1, size):
            if list1[j] < list1[min_index]:
                min_index = j

        (list1[index], list1[min_index]) = (list1[min_index], list1[index])

print("Enter List: ")

list1 = list(map(int,input().split(',')))
size = len(list1)
selectionSort(list1)
print('The list after sorting in Ascending Order by selection sort is:')
print(list1)