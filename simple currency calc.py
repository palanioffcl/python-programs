a = []
a = [int(i) for i in input("Enter amount with spaces : ").split()]

print("="*18)
print(" 10   x ",a.count(10),"  =",a.count(10)*10)
print(" 20   x ",a.count(20),"  =",a.count(20)*20)
print(" 50   x ",a.count(50),"  =",a.count(50)*50)
print(" 100  x ",a.count(100)," =",a.count(100)*100)
print(" 500  x ",a.count(500)," =",a.count(500)*500)
print(" 2000 x ",a.count(2000),"=",a.count(2000)*2000)
print(" Total  = ",sum(a),"/-")
print("="*18)
