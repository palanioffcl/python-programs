tam = int(input("Enter your Tamil Mark = "))
eng = int(input("Enter your English Mark = "))
mat = int(input("Enter your Maths Mark = "))
sci = int(input("Enter your Science Mark = "))
soc = int(input("Enter your Social  Mark = "))

avg = (tam+eng+mat+sci+soc)/5

if avg >= 95 or avg == 100:
  print("You Secured A Grade")
elif avg < 95 or avg >= 80:
  print("You Secured B Grade")
elif avg < 80 or avg <= 60:
  print("You Secured C Grade")
elif avg < 60 or avg == 40:
  print("You Secured D Grade")
else:
  print("You didnt secured any grade")
