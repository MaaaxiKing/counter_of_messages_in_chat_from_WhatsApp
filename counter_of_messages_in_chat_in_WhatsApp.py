import sys
import re
f = open(sys.argv[1], "r", encoding='utf-8')
lines = f.readlines()
count_of_messages = 0
for line in lines:
    if re.match("[1-9]|1[0-2]/[1-9]|[12][0-9]|3[01]/\d{2} [0-2][0-9]:[0-5][0-9] - ", line):
        count_of_messages += 1
print(f"{count_of_messages} messages")