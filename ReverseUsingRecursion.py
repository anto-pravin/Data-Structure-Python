def reverse(l,n):
    if n < 0:
        return l
    else:
        k = l.pop(0)
        l.insert(n,k)
        return reverse(l,n-1)
length = int(input())
list = list(map(int,input().split()))
print(*reverse(list,length-1))