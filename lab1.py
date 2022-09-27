# Empty list is created
l=[]

# input from user (size)
k = int(input("Enter the size : "))

# elements insertion
for i in range(k):
    l.append(int(input("Enter element : ")))

# insertion sort algorithm
for i in range(1,len(l)):
    val=l[i]
    j = i-1
    while j>=0 and val<l[j] :
            l[j+1] = l[j]
            j = j-1
    l[j+1] = val

print(l)

# input from user for binary search
target = int(input("Enter the target : "))

# Binary search algorithm
low = 0
high = len(l)-1

while low<=high:
    guess = (high+low)//2
    if l[guess]==target:
        print('Found at index ', guess)
        break
    elif l[guess]>target:
        high=guess-1
    else:
        low=guess+1
