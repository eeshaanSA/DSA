# Write a python program to store roll numbers of student in array who attended training program in random order. 
# Write function for searching whether particular student attended training program or not, using
# Linear search and Sentinel search.
# b) Write a python program to store roll numbers of student array who attended training program in sorted order.
# Write function for searching whether particular student attended training program or not, using Binary search and Fibonacci search.

def linear_search(a,n,c):
    for i in range(n):
        if c == a[i]:
            print(c, "is present at index", i)
            print("student was present in program.")
            break
        else:
            print("student was absent in program.")


def sentinelSearch(a, n, c):
    last = a[n - 1]
    a[n - 1] = c
    i = 0

    while (a[i] != c):
        i += 1
    a[n - 1] = last

    if ((i < n - 1) or (a[n - 1] == c)):
        print(c, "is present at index", i)
        print("student was present in program.")
    else:
        print("student was absent in program.")

n=int(input("Enter the number of students:"))
a=[]

print("Enter the roll no.:")
for i in range(n):
    b=int(input())
    a.append(b)
print("List of student roll no. present in program:")
print(a,"\n")

c=int(input("enter the roll no. to search a student:"))
print("Select the searching method:")
print("1.Linear Search.\n2.Sentinal Search.")

d=int(input())

if (d==1):
    linear_search(a,n,c)
else:
    sentinelSearch(a,n,c)
