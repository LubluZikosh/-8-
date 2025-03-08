arr = [3, 8, 2, 10, 5]
average = sum(arr) / len(arr)
result = [x for x in arr if x < average]
print(result)





start = int(input("start "))
n = int(input(" n"))
total = sum(range(start, start + n))
print(total)





arr = [3, 8, 2, 3, 4, 8, 2]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
arr[:] = unique
print(arr   )



arr = [3, 8, 2, 4]
found = any(arr[i] + arr[j] == 12 for i in range(len(arr)) for j in range(i + 1, len(arr)))
print(found)    
