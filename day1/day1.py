data = open("input.txt").read().splitlines()

x = 0
for i in data:
    x += int(i)
print("Part 1:", x)

freqs = set()
x = 0
index = 0
max_index = len(data)
while x not in freqs:
    freqs.add(x)
    x += int(data[index % max_index])
    index += 1

print("Part 2:", x)
