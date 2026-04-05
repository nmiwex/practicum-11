nums = list(map(int, input().split()))
even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += num
    else:
        odd += num

print(even, odd)