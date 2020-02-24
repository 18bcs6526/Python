'''n=int(input("enter the number to check palindrome"))
rev=0
temp=n
for i in range (n+1):
    rem=n%10
    rev=rev*10+rem
    n=n//10



if(temp==n):
    print("number is pallidrome")
else:
    print("not a pallindrome")

#logic string

def isPalindrome(str):
    for i in xrange(0, len(str) / 2):
        if (str[i] != str[len(str) - i - 1]):
            return False
            return True

x="priyanshu"
y = isPalindrome(x)

if (y):
    print("Yes")
else:
    print("No")
'''

#using reversed key word
'''def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return 1
    return 0


x = str(input("enter the string"))
a = isPalindrome(x)

if (a):
    print("Yes")
else:
    print("No")
'''

x=(str(input("enter the string")))
rev=("".join(reversed(x)))
print(rev)
if(x==rev):
    print("palladrome")

