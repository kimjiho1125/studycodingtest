Words = list(input())
count = 0
for x in Words:
    if (x == "A" or x == "B" or x == "C"):
        count += 3
    elif (x == "D" or x == "E" or x == "F"):
        count += 4
    elif (x == "G" or x == "H" or x == "I"):
        count += 5
    elif (x == "J" or x == "K" or x == "L"):
        count += 6
    elif (x == "M" or x == "N" or x == "O"):
        count += 7
    elif (x == "Q" or x == "P" or x == "R" or x == "S"):
        count += 8
    elif (x == "T" or x == "U" or x == "V"):
        count += 9
    else:
        count += 10

print(count)