# "Fundamental of Data
# Structure" by N students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency

def get_arr(li,n):
    i=0
    print("Enter the marks:")
    while i<n:
        a=int(input())
        if a<=100 and a>=-1:
            li.append(a)
            i+=1
        else:
            print("Enter the number between 0 to 100")
    print("List of marks scored by student:")
    print(li,"\n")
def Max(li,N):
    maxa=-4
    for i in range(N):
        if li[i]>maxa:
            maxa=li[i]
    print("Highest score:",maxa)
def Min(li,N):
    mina=101
    for i in range(N):
        if li[i]<mina and li[i]!=-1:
            mina=li[i]
    print("Lowest score:",mina)
def frq(li,N):
    occ=0
    b=0
    for i in range (N):
        count=0
        for j in range(N):
            if li[i]==li[j]:
                count+=1
        if li[i]!=-1 and count>occ:
            occ=count
            b=li[i]
    if (occ!=1):
        print("Marks with highest frequency:",b)
    else:
        print("Marks with highest frequency:none")
def avg(li,N):
    sum = 0
    count = 0
    for i in range(N):
        if li[i] != -1:
            sum = sum + li[i]
    else:
        count += 1
    avg = sum / (N - count)
    print("Average score of class:", avg)
    print("Number of absent students:", count)
N=int(input("Enter number of students:"))
li=[]
get_arr(li,N)
avg(li,N)
Max(li,N)
Min(li,N)
frq(li,N)
