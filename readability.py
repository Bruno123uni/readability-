from cs50 import get_string

text = get_string("Text: ")
l = len(text)
h = 0
e = 0

for g in range(l):
    if text[g] >= "a" and text[g] <= 'z':
        h += 1
    elif text[g] >= 'A' and text[g] <= 'Z':
        h += 1
e = 1
for t in range(l):
    if text[t] == ' ':
        e += 1
qw = 0
for q in range(l):
    if text[q] == ".":
        qw += 1
    elif text[q] == '?':
        qw += 1
    elif text[q] == '!':
        qw += 1
S = (qw / e) * 100
L = (h / e) * 100
Index12 = 0.0588 * L - 0.296 * S - 15.8
Index = (round(Index12))
if Index12 < 1:
    print("Before Grade 1")
elif Index12 > 15:
    print("Grade 16+")
else:
    print("Grade ", end="")
    print(Index)