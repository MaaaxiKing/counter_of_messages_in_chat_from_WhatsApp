import sys
import re
file = open(sys.argv[1], "r", encoding='utf-8')
lines = file.readlines()
count_of_messages = 0
IDs = set()
counts_of_messages_by_ID = {}
separator_between_time_and_ID = " - "
pattern_for_time = r"([1-9]|(1[0-2]))/([1-9]|([12][0-9])|(3[01]))/\d{2}, (([01][0-9])|(2[0-3])):[0-5][0-9]"
for line in lines:
    signature = re.match(f"(?={pattern_for_time}{separator_between_time_and_ID}).+?(?=: .+)", line)
    if signature:
        ID = signature.group().replace(re.match(pattern_for_time + separator_between_time_and_ID, line).group(), '')
        count_of_messages += 1
        IDs.add(ID)
        counts_of_messages_by_ID[ID] = 1 if not ID in counts_of_messages_by_ID.keys() else counts_of_messages_by_ID[ID] + 1
print(f"{count_of_messages} messages")
for ID in counts_of_messages_by_ID.keys():
    print(f"{ID}: {counts_of_messages_by_ID[ID]} messages")