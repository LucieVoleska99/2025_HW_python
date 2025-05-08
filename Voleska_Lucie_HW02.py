import json
import math

with open('netflix_titles.tsv', encoding='utf-8') as file:
    whole_text = file.read()

netflix_lines = whole_text.split('\n')  


def empty_list(value):
    value = value.strip()
    if value == '':
        return []
    else:
        return [value]
    
column_key = ['PRIMARYTITLE', 'DIRECTOR', 'CAST', 'GENRES', 'STARTYEAR']
index_dict = dict()
count_index = -1

for line in netflix_lines:
    netflix_text = line.split('\t')
    for bunka in netflix_text:
        count_index += 1
        if bunka in column_key:
            index_dict[bunka] = count_index
    break


netflix_final = []
count_index = 0
for line in netflix_lines:
    if count_index == 0:
        count_index += 1
        continue
    netflix_text = line.split('\t')
    netlix_film = {
        'title': netflix_text[index_dict['PRIMARYTITLE']],
        'directors': empty_list(netflix_text[index_dict['DIRECTOR']]),
        'cast': empty_list(netflix_text[index_dict['CAST']]),
        'genres': empty_list(netflix_text[index_dict['GENRES']]),
        'decade': math.floor(int(netflix_text[index_dict['STARTYEAR']]) / 10) * 10}
    netflix_final.append(netlix_film)


with open('Voleska_Lucie_HW02.json', mode='w', encoding='utf-8') as output_file:
    json.dump(netflix_final, output_file, ensure_ascii=False, indent=4)
