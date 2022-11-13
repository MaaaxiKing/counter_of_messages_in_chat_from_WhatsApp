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
names_of_languages_in_use = ["english", "german", "french", "spanish", "afrikaans", "albanian", "catalan", "croatian", "czech", "danish", "dutch", "estonian", "filipino", "finnish", "italian"]
patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time = {
    "M": r"([1-9]|(1[0-2]))", 
    "D": r"([1-9]|([12][0-9])|(3[01]))", 
    "YY": r"\d{2}", 
    "HH": r"(([01][0-9])|(2[0-3]))", 
    "mm": r"[0-5][0-9]", #minutes, not 2-digit month; provisorical
    "DD": r"(([0-2][0-9])|(3[01]))", 
    "MM": r"((0[1-9])|(1[0-2]))", 
    "YYYY": r"\d{4}", 
    "H": r"((1?[0-9])|(2[0-3]))"
}
patterns_as_regex_for_time_by_pattern_for_time = {
    "M/D/YY, HH:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"M"]}/{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"D"]}/{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YY"]}, {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"HH"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "DD.MM.YY, HH:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"DD"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"MM"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YY"]}, {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"HH"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "DD/MM/YYYY à HH:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"DD"]}/{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"MM"]}/{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YYYY"]} à {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"HH"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "D/M/YY H:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"D"]}/{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"M"]}/{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YY"]} {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"H"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "YYYY-MM-DD H:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YYYY"]}-{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"MM"]}-{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"DD"]} {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"H"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "D.M.YY, HH:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"D"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"M"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YY"]}, {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"HH"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "D/M/YY, H:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"D"]}/{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"M"]}/{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YY"]}, {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"H"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "DD. MM. YYYY. HH:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"DD"]}/. {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"MM"]}/. {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YYYY"]}. {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"HH"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"MM"]}""", 
    "DD.MM.YY H:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"DD"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"MM"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YY"]} {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"H"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "DD.MM.YYYY HH.MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"DD"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"MM"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YYYY"]} {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"HH"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "DD-MM-YYYY HH:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"DD"]}-{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"MM"]}-{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YYYY"]} {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"HH"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "DD.MM.YY HH:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"DD"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"MM"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YY"]} {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"HH"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "D.M.YYYY klo H.MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"D"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"M"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YYYY"]} klo {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"H"]}\.{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}""", 
    "DD/MM/YY, HH:MM": f"""{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"DD"]}/{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"MM"]}/{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"YY"]}, {patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"HH"]}:{patterns_as_regex_for_element_of_time_by_abbreviation_for_element_of_time[r"mm"]}"""
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
counts_of_messages_by_ID_sorted_by_count_as_list = sorted(counts_of_messages_by_ID.items(), key=lambda item: item[1])
counts_of_messages_by_ID_sorted_by_symbol_1_of_ID_as_list = sorted(counts_of_messages_by_ID.items(), key=lambda item: item[0])
counts_of_messages_by_ID_sorted_by_symbol_1_of_ID = dict(sorted(counts_of_messages_by_ID.items(), key=lambda item: item[0]))
if list(counts_of_messages_by_ID) == counts_of_messages_by_ID_sorted_by_count_as_list:
    print("\r\nsorted by first message and message count simultaneously\r\n")
    print_ID_with_assignment_to_corresponding_count_of_messages()
else:
    print("\r\nsorted by first message\r\n")
    print_ID_with_assignment_to_corresponding_count_of_messages()
    print("\r\nsorted by message count\r\n")
    counts_of_messages_by_ID_sorted_by_count = dict(counts_of_messages_by_ID_sorted_by_count_as_list)
    for ID in counts_of_messages_by_ID_sorted_by_count.keys():
        print(f"{ID}: {counts_of_messages_by_ID[ID]} messages – {counts_of_messages_by_ID[ID] / count_of_messages * 100} %")
