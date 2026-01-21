import sys

for line in sys.stdin:
    if line.strip() == "":
        continue
    nums = list(map(int, line.split()))
    print(min(nums))
