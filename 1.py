fst_lst = []
sec_lst = []

for _ in range(10):
    fst_lst.append(int(input()))
for i in range(8):
    sec_lst.append(fst_lst[i] + fst_lst[i+1])

print(sec_lst)