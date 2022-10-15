#import os
#os.system(f"{os.getcwd()}/{os.path.basename(__file__)}")
import sys
import re
file = open(sys.argv[1], "r", encoding='utf-8')
lines = file.readlines()
count_of_messages = 0
IDs = set()
counts_of_messages_by_ID = {}
separator_between_time_and_ID = " - "
patterns_for_time_by_name_of_language = {
    "english": r"([1-9]|(1[0-2]))/([1-9]|([12][0-9])|(3[01]))/\d{2}, (([01][0-9])|(2[0-3])):[0-5][0-9]", 
    "german": r"((0[1-9])|([12][0-9])|(3[01]))\.((0[1-9])|(1[0-2]))\.\d{2}, (([01][0-9])|(2[0-3])):[0-5][0-9]", 
    "french": r"((0[1-9])|([12][0-9])|(3[01]))/((0[1-9])|(1[0-2]))/\d{4} à (([01][0-9])|(2[0-3])):[0-5][0-9]", 
    "spanish": r"([1-9]|([12][0-9])|(3[01]))/([1-9]|(1[0-2]))/\d{2} ((1?[0-9])|(2[0-3])):[0-5][0-9]",
    "afrikaans": r"\d{4}-((0[1-9])|(1[0-2]))-((0[1-9])|([12][0-9])|(3[01])) ((1?[0-9])|(2[0-3])):[0-5][0-9]",
    "albanian": r"([1-9]|([12][0-9])|(3[01]))\.([1-9]|(1[0-2]))\.\d{2}, (([01][0-9])|(2[0-3])):[0-5][0-9]",
    "català": r"([1-9]|([12][0-9])|(3[01]))/([1-9]|(1[0-2]))/\d{2}, ((1?[0-9])|(2[0-3])):[0-5][0-9]"
}
if len(sys.argv) >= 3:
    pattern_for_time = patterns_for_time_by_name_of_language[sys.argv[2]]
else:
    languages_by_pattern_of_filename = {}
    #match sys.argv[1]:
    #    case re.match(
    pattern_for_time = patterns_for_time_by_name_of_language["english"]    
def print_ID_with_assignment_to_corresponding_count_of_messages():
    for ID in counts_of_messages_by_ID.keys():
        print(f"{ID}: {counts_of_messages_by_ID[ID]} messages")
for line in lines:
    signature = re.match(f"(?={pattern_for_time}{separator_between_time_and_ID}).+?(?=: .+)", line)
    if signature:
        ID = signature.group().replace(re.match(pattern_for_time + separator_between_time_and_ID, line).group(), '')
        count_of_messages += 1
        IDs.add(ID)
        counts_of_messages_by_ID[ID] = 1 if not ID in counts_of_messages_by_ID.keys() else counts_of_messages_by_ID[ID] + 1
print(f"{count_of_messages} messages overall")
if counts_of_messages_by_ID == dict(sorted(counts_of_messages_by_ID.items(), key=lambda item: item[1])):
    print("\r\nsorted by first message and message count simultaneously\r\n")
    print_ID_with_assignment_to_corresponding_count_of_messages()
else:
    print("\r\nsorted by first message\r\n")
    print_ID_with_assignment_to_corresponding_count_of_messages()
    print("\r\nsorted by message count\r\n")
    for ID in counts_of_messages_by_ID.keys():
        print(f"{ID}: {dict(sorted(counts_of_messages_by_ID.items(), key=lambda item: item[1]))[ID]} messages")
