n = int(input())
words = input().split(",")
pattern = input()
result = []
for word in words:
    abbr = ""
    for ch in word:
        if ch.isupper():
            abbr += ch
    if abbr.startswith(pattern):
        result.append((abbr, word))
if len(result) == 0:
    print("No match found")
else:
    result.sort()
    for abbr, word in result:
        print(word)
