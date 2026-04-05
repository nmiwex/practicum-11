num = int(input())
dividers = []

for i in range(1,  num + 1):
    if num % i == 0:
        dividers.append(i)

print(dividers)