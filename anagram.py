w1 = raw_input()
w2 = raw_input()

total = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter in w1 and letter not in w2 or letter not in w1 and letter in w2 :
        total += 1
print total

