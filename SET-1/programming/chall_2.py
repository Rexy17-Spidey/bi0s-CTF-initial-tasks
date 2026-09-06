data = input().strip()

list_part, target_part = data.rsplit("]", 1)

numbers = list(map(int, list_part.strip("[").split(",")))
target = int(target_part.strip())

# Bubble Sort
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

# Binary Search
left = 0
right = len(numbers) - 1
found = False

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        found = True
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print(found)