#create a list 
list1= ["apple","banana","cherry","tomato","guava","pear","mango"]

#Accessing elements from the list
print(list1[0])
print(list1[1])
print(list1[2]) 

#Negative Indexing
print(list1[-1])
print(list1[-2])
print(list1[-3])

# slicing
print(list1[2:4])

#2D Lists
matrix= [[1,2,3],[4,5,6],[7,8,9]]

for i in range(0, len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j],end= "")
    print("\n")