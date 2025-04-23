import re
import json
with open('alice.txt', encoding='utf-8') as file:
    text = file.read()

char_list = []  
for char in text:
    if re.match(r"[A-Z]", char):
        char_list.append(char.lower())
    else:
        if char not in [' ', '\n']:
            char_list.append(char)    

char_counts = dict()
for char in char_list:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1
sorted_counts = dict(sorted(char_counts.items()))


with open('Voleska_Lucie_HW01.json', mode='w', encoding='utf-8') as output_file:
    json.dump(sorted_counts, output_file, ensure_ascii=False, indent=4)






