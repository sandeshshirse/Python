arr = [1, 2, 3, 4, 5]

# reverse array
rev = []
i = len(arr) - 1
while i >= 0:
    rev.append(arr[i])
    i = i - 1

# average
total = 0
for x in arr:
    total = total + x

avg = total / len(arr)

print("Reversed:", rev)
print("Average:", avg)
