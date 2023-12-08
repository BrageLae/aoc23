# PART 1
def is_legal_amount(number, word):
    max_colors = {"red": 12, "green": 13, "blue": 14}
    return max_colors[word] >= number


with open("input.txt") as file:
    lines = file.readlines()

sum = 0
for i, line in enumerate(lines):
    flag = True
    for set in line.split(":")[-1].replace(",", "").split(";"):
        for word in set.strip().split(" "):
            if word.isdigit():
                number = int(word)
            else:
                if not is_legal_amount(number, word):
                    flag = False
    if flag:
        sum += i + 1

print(sum)

# PART 2
minimum_colors = {"red": 0, "green": 0, "blue": 0}

sum = 0
for i, line in enumerate(lines):
    for set in line.split(":")[-1].replace(",", "").split(";"):
        for word in set.strip().split(" "):
            if word.isdigit():
                number = int(word)
            else:
                minimum_colors[word] = max(minimum_colors[word], number)
    power = 1
    for x in minimum_colors.values():
        power *= x

    sum += power
    minimum_colors = {"red": 0, "green": 0, "blue": 0}

print(sum)
