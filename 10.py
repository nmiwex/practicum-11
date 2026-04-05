lst1 = list(input().split())
lst2 = list(input().split())
fr, to = map(int, input().split())
for i in range(to, fr-1, -1):
    lst2.append(lst1.pop(i))
print(lst1)
print(lst2)