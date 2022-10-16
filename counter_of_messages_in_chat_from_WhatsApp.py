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
patterns_as_regex_for_time_by_pattern_for_time = {
    "M/D/YY, HH:MM": r"([1-9]|(1[0-2]))/([1-9]|([12][0-9])|(3[01]))/\d{2}, (([01][0-9])|(2[0-3])):[0-5][0-9]", 
    "DD.MM.YY, HH:MM": r"((0[1-9])|([12][0-9])|(3[01]))\.((0[1-9])|(1[0-2]))\.\d{2}, (([01][0-9])|(2[0-3])):[0-5][0-9]", 
    "DD/MM/YYYY à HH:MM": r"((0[1-9])|([12][0-9])|(3[01]))/((0[1-9])|(1[0-2]))/\d{4} à (([01][0-9])|(2[0-3])):[0-5][0-9]", 
    "D/M/YY H:MM": r"([1-9]|([12][0-9])|(3[01]))/([1-9]|(1[0-2]))/\d{2} ((1?[0-9])|(2[0-3])):[0-5][0-9]", 
    "YYYY-MM-DD H:MM": r"\d{4}-((0[1-9])|(1[0-2]))-((0[1-9])|([12][0-9])|(3[01])) ((1?[0-9])|(2[0-3])):[0-5][0-9]", 
    "D.M.YY, HH:MM": r"([1-9]|([12][0-9])|(3[01]))\.([1-9]|(1[0-2]))\.\d{2}, (([01][0-9])|(2[0-3])):[0-5][0-9]", 
    "D/M/YY, H:MM": r"([1-9]|([12][0-9])|(3[01]))/([1-9]|(1[0-2]))/\d{2}, ((1?[0-9])|(2[0-3])):[0-5][0-9]", 
    "DD. MM. YYYY. HH:MM": r"((0[1-9])|([12][0-9])|(3[01]))\. ((0[1-9])|(1[0-2]))\. \d{4}. (([01][0-9])|(2[0-3])):[0-5][0-9]", 
    "DD.MM.YY H:MM": r"((0[1-9])|([12][0-9])|(3[01]))\.((0[1-9])|(1[0-2]))\.\d{2} ((1?[0-9])|(2[0-3])):[0-5][0-9]", 
    "DD.MM.YYYY HH.MM": r"((0[1-9])|([12][0-9])|(3[01]))\.((0[1-9])|(1[0-2]))\.\d{4} (([01][0-9])|(2[0-3])).[0-5][0-9]", 
    "DD-MM-YYYY HH:MM": r"((0[1-9])|([12][0-9])|(3[01]))-((0[1-9])|(1[0-2]))-\d{4} (([01][0-9])|(2[0-3])):[0-5][0-9]", 
    "DD.MM.YY HH:MM": r"((0[1-9])|([12][0-9])|(3[01]))\.((0[1-9])|(1[0-2]))\.\d{2} (([01][0-9])|(2[0-3])):[0-5][0-9]", 
    "D.M.YYYY klo H.MM": r"([1-9]|([12][0-9])|(3[01])).([1-9]|(1[0-2])).\d{4} klo ((1?[0-9])|(2[0-3])).[0-5][0-9]",
    "DD/MM/YY, HH:MM": r"((0[1-9])|([12][0-9])|(3[01]))/((0[1-9])|(1[0-2]))/\d{2}, (([01][0-9])|(2[0-3])):[0-5][0-9]"
}
patterns_for_time_by_name_of_language = {
    "english": patterns_as_regex_for_time_by_pattern_for_time["M/D/YY, HH:MM"], 
    "german": patterns_as_regex_for_time_by_pattern_for_time["DD.MM.YY, HH:MM"], 
    "french": patterns_as_regex_for_time_by_pattern_for_time["DD/MM/YYYY à HH:MM"], 
    "spanish": patterns_as_regex_for_time_by_pattern_for_time["D/M/YY H:MM"], 
    "afrikaans": patterns_as_regex_for_time_by_pattern_for_time["YYYY-MM-DD H:MM"], 
    "albanian": patterns_as_regex_for_time_by_pattern_for_time["D.M.YY, HH:MM"], 
    "catalan": patterns_as_regex_for_time_by_pattern_for_time["D/M/YY, H:MM"], 
    "croatian": patterns_as_regex_for_time_by_pattern_for_time["DD. MM. YYYY. HH:MM"], 
    "czech": patterns_as_regex_for_time_by_pattern_for_time["DD.MM.YY H:MM"], 
    "danish": patterns_as_regex_for_time_by_pattern_for_time["DD.MM.YYYY HH.MM"], 
    "dutch": patterns_as_regex_for_time_by_pattern_for_time["DD-MM-YYYY HH:MM"], 
    "estonian": patterns_as_regex_for_time_by_pattern_for_time["DD.MM.YY HH:MM"], 
    "filipino": patterns_as_regex_for_time_by_pattern_for_time["M/D/YY, HH:MM"], 
    "finnish": patterns_as_regex_for_time_by_pattern_for_time["D.M.YYYY klo H.MM"], 
    "italian": patterns_as_regex_for_time_by_pattern_for_time["DD/MM/YY, HH:MM"]
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
