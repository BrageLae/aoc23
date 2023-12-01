import re

# PART 1

with open("input.txt") as file:
    numbers = []
    for line in file:
        digits = re.findall("[0-9]", line)
        numbers.append(int("".join([digits[0], digits[-1]])))

print(sum(numbers))

# PART 2

word_names = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("input.txt") as file:
    numbers = []
    for line in file:
        digits = re.findall(f"(?=([0-9]|{"|".join(word_names.keys())}))", line)
        digits = [word_names[x] if x in word_names.keys() else x for x in digits]
        numbers.append(int("".join([digits[0], digits[-1]])))

print(sum(numbers))
