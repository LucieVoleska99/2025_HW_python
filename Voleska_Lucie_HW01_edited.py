import json

with open('alice.txt', encoding='utf-8') as file:
    text = file.read()

text = text.replace(' ', '').replace('\n', '')
text = text.lower()

char_counts = dict()
for char in text:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

with open('Voleska_Lucie_HW01_edited.json', mode='w', encoding='utf-8') as output_file:
    json.dump(char_counts, output_file, ensure_ascii=False, sort_keys=True, indent = 4)




