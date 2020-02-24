x = int(input("enter the number"))
y = int(input("enter the second number"))
if x>y:
    min=y
else:
    min=x

for i in range(min,1,-1):
    if x%i == 0 and y%i == 0:
        gcd = i
        break
print(gcd)
