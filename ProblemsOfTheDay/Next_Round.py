a, b = map(int, input().split())
l = list(map(int, input().split()))
val = l[b-1]; c = 0

for i in l:
    if i >= val and i:
        c += 1 

print(c)