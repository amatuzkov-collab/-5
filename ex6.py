a=int(input())
b=int(input())
c=int(input())
k=0
if a==c and a!=b:
    k=2
if b==c and a!=b:
    k=2
if a==b and b!=c:
    k=2
if a!=b and b!=c and a!=c:
    k=1
if a==b==c:
    k=3
print(k)
