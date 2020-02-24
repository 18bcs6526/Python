n = int(input())
arr = list(input().split())
largest = max(arr)

for i in range(n):
    if largest == max(arr):
        arr.remove(max(arr))

print(max(arr))