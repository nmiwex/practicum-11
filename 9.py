lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line.lower())

text = '\n'.join(lines)
all_words = text.split()
words = []

for word in all_words:
    clean = ''
    for ch in word:
        if ch.isalpha():
            clean += ch
    if clean:
        words.append(clean)

count = {}
order = {}
pos = 0

for word in words:
    if word not in count:
        count[word] = 0
        order[word] = pos
        pos += 1
    count[word] += 1

sorted_words = sorted(count.keys(), key=lambda w: (-count[w], order[w]))

for word in sorted_words:
    print(word)