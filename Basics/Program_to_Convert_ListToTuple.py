# Program to convert List into a Tuple

list=[]
n=int(input("Enter Limit of list"))
for items in range(0,n):
    num=int(input("Enter value"))
    list.append(num)
print(list)    
new_tuple=tuple(list)
print("Tuple:",new_tuple)