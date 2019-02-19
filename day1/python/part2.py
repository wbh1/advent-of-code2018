import sys

i = 0

# Use a set for this. The performance hit of a list is ridiculous when compared to a set.
pastValues = set()
repeats = 0

while repeats < 200:
    with open("../changes.txt") as f:
        for line in f:
            value = int(line[1:])
            if line[0] == "+":
                i += value
            elif line[0] == "-":
                i -= value
            else:
                raise ValueError("cannot parse: '{0}' as a sign".format(line[0]))

            # This is the part where a "set" really shines
            if i in pastValues:
                print("{0} repeated.".format(i))
                sys.exit(0)
            else:
                pastValues.add(i)
        f.seek(0, 0)
        repeats += 1