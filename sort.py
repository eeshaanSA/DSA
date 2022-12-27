# Write a python program to store first year percentage of students in array. Write function
# for sorting array of floating point numbers in ascending order using
# a) Selection Sort
# b) Bubble sort and display top five scores
def sel_sort(arr, size):
    for i in range(size-1):
        min_index = i
        for j in range(i+1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

def bubble_sort(arr, size):
    for i in range(size):
        for j in range(1, size-i):
            if arr[j-1] > arr[j] :
                arr[j-1], arr[j] = arr[j], arr[j-1]
    
    return arr

def inp_op():
    operation = int(input(("\n'1' for Selection sort(atleast 7)/\n'2' for Bubble sort:" )))
    if operation != 1 and operation != 2:
        print('Invalid operation')
        inp_op()

    return operation

operation = inp_op()

n = int(input("Enter number of elements in the arr: "))
inpArr = []

for i in range(n):
    inpArr.append(int(input("Enter element " + str(i+1) + ": ")))

if operation == 1:
    
    print("\nThis is using selection sort: ")
    sel_sort(inpArr, n)
    print("\nTop 5 scores are: ")
    for i in range(5):
        print("Rank " + str(i+1) + " : " + str(inpArr[n-1-i]) + "%")

else:
    
    print("\nThis is using bubble sort")
    bubble_sort(inpArr, n)
    print("\nTop 5 scores are: ")
    for i in range(5):
        print("Rank " + str(i+1) + " : " + str(inpArr[n-1-i]) + "%")
