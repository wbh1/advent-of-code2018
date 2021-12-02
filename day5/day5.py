from string import ascii_lowercase

data = None

with open("input.txt") as f:
    data = f.read().strip()


def opposites(a, b):
    return (a.lower() == b.lower()) and (a != b)


def react(polymer: str):
    buffer = []

    for ltr in polymer:
        if buffer and opposites(ltr, buffer[-1]):
            buffer.pop()
        else:
            buffer.append(ltr)
    return buffer


print("Part 1:", len(react(data)))

permutations = {ltr: data for ltr in ascii_lowercase}

for ltr in permutations.keys():
    permutations[ltr] = permutations[ltr].replace(ltr, "")
    permutations[ltr] = permutations[ltr].replace(ltr.upper(), "")
    permutations[ltr] = react(permutations[ltr])

SHORTEST = 0
for unit, polymer in permutations.items():
    if SHORTEST == 0:
        SHORTEST = len(polymer)
    elif len(polymer) < SHORTEST:
        SHORTEST = len(polymer)

print("Part 2:", SHORTEST)
