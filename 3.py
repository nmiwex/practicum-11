string = input().split()
clean_words = []

for word in string:
    clean = ''

    for ch in word:
        if ch.isalpha():
            clean += ch
    if clean:
        clean_words.append(clean)

print(clean_words)