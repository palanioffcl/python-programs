lst = []

n = int(input("Enter no of elements"))

for i in range(0,n):
   element = eval(input())
   lst.append(element)

avg = sum(lst)/len(lst)

print("The Average of Array is = ", avg)
