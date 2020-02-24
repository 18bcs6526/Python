n=int (input("enter the number to find factorial"))
def fact(n):
    if (n==1):
        return n
    else:
        return (n*(fact(n-1)))
print(fact(n))