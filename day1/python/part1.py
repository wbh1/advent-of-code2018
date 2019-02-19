INITIAL = 0

with open("../changes.txt") as f:
    lines = 0
    for line in f:
        if line[0] == "+":
            INITIAL += int(line[1:])
            lines += 1
        elif line[0] == "-":
            INITIAL -= int(line[1:])
            lines += 1
        else:
            raise ValueError("cannot parse: '{0}' as a sign".format(line[0]))
print(INITIAL)
