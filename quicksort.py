# Write a Python program to store first year percentage of students in array. 
# Write function for sorting array of floating point numbers in ascending order using quick sort and display top five scores

n = int(input("\nEnter number of elements in the arr(atleast 7): "))
inpArr = []

for i in range(n):
    inpArr.append(float(input("Enter element " + str(i+1) + ": ")))

def partition(arr, low, high):
    pivot = arr[high]
    pointer = low-1

    for i in range(low, high+1):
        if arr[i] <= pivot:
            pointer += 1
            arr[i], arr[pointer] = arr[pointer], arr[i]

    return pointer

def quicksort(arr, low, high):
    if low < high: 

        fixed = partition(arr, low, high)

        quicksort(arr, low, fixed-1)
        quicksort(arr, fixed+1, high)

        return arr

    else:
        return arr

quicksort(inpArr, 0, n-1)
print("\nTop 5 scores are: ")
for i in range(5):
    print("Rank " + str(i+1) + " : " + str(inpArr[n-i-1]) + "%")
