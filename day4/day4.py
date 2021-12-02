from collections import Counter
from datetime import datetime
import re

guards = {}
data = []

parser = re.compile(
    r"\[([\d\-: ]+)\] (falls asleep|wakes up|Guard #(\d+) begins shift)"
)

with open("day4.txt") as f:
    data = f.read()

matches = parser.findall(data)

logs = {datetime.strptime(m[0], "%Y-%m-%d %H:%M"): (m[1], m[2]) for m in matches}
sorted_ts = sorted(logs)

ON_DUTY = 0
ASLEEP = datetime.now().minute
for i, ts in enumerate(sorted_ts):
    msg = logs[ts]
    if msg[1]:
        ON_DUTY = msg[1]
        if msg[1] not in guards.keys():
            guards[msg[1]] = Counter()
    elif "asleep" in msg[0]:
        ASLEEP = ts.minute
    elif "wakes" in msg[0]:
        guards[ON_DUTY].update([m for m in range(ASLEEP, ts.minute)])

MAX_ASLEEP = 0
MAX_SLEEPER = 0
for guard, sleepytime in guards.items():
    sleepytime: Counter
    mins_asleep = sum(sleepytime.values())
    if mins_asleep > MAX_ASLEEP:
        MAX_ASLEEP = mins_asleep
        MAX_SLEEPER = guard

print(
    f"{MAX_SLEEPER} slept for {MAX_ASLEEP} mins.",
    f"Usually at {guards[MAX_SLEEPER].most_common(1)[0]}",
)
print("Part 1:", int(MAX_SLEEPER) * guards[MAX_SLEEPER].most_common(1)[0][0])

MAX_ASLEEP = (0, 0)
MAX_SLEEPER = 0
guards_sleeping_most = {
    guard: sleepytime.most_common(1) for guard, sleepytime in guards.items()
}
for g, sleepin in guards_sleeping_most.items():
    if len(sleepin):
        if sleepin[0][1] > MAX_ASLEEP[1]:
            MAX_ASLEEP = sleepin[0]
            MAX_SLEEPER = g

print(f"{MAX_SLEEPER} slept most usually at {MAX_ASLEEP}")
print("Part 2:", int(MAX_SLEEPER) * guards_sleeping_most[MAX_SLEEPER][0][0])
