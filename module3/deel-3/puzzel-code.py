reeks = "1"
print(reeks)

while "33" not in reeks:
    result = ""
    count = 1
    for i in range(1, len(reeks)):
        if reeks[i] == reeks[i - 1]:
            count += 1
        else:
            result += str(count) + reeks[i - 1]
            count = 1
    result += str(count) + reeks[-1]
    reeks = result
    print(reeks)
