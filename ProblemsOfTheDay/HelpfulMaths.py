str1 = input().lower()
arr = [i for i in str1 if i.isdigit()]
arr.sort()
print('+'.join(arr))