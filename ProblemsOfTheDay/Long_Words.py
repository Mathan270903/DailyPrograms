int_val = int(input())
arr = []

while int_val:
    str_val = input()
    arr.append(str_val)
    int_val -= 1

for i in arr:
    length = len(i)
    if length > 10:
        print(f"{i[0]}{length-2}{i[length-1]}")
    else:
        print(i)