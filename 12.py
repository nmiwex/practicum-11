def count_holes(word):
    """
    counts the number of holes in a word
    """
    holes = 'abdegopq'
    cnt = 0
    for ch in word:
        if ch in holes:
            cnt += 1
    return cnt


s = input().strip()
words = s.split()

holes = 0
noholes = 0
two_or_more = []

for w in words:
    h = count_holes(w)
    holes += h
    noholes += len(w) - h
    if h >= 2:
        two_or_more.append(w)

print(holes, noholes)
print(two_or_more)