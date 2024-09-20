int_val = int(input())
arr = []; val = 0
add = '+'

while int_val:
    str_val = input()
    arr.append(str_val)
    int_val -= 1

for i in arr:
    if add in i:
        val += 1 
    else:
        val -= 1
print(val)