lst = []

n = int(input("Enter no of elements"))

for i in range(0,n):
   element = eval(input())
   lst.append(element)

for i in lst:
  if i%2 == 0:
    print("Even Value")
  else:
    print("Odd value")
