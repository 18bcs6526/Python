a=0
b=1
x=int (input("enter the number"))
print('0')
for i in range (0,x):
    c=a+b
    a=b
    b=c
    print(c)