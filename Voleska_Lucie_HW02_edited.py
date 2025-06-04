import json

with open('netflix_titles.tsv', encoding='utf-8') as file:
    whole_text = file.read()

netflix_lines = whole_text.split('\n')  

    
def empty_list(value):
    value = value.strip()
    if value == '':
        return []
    else:
        result = []
        items = value.split(',')
        for item in items:
            stripped_item = item.strip()
            result.append(stripped_item)
        return result


column_key = ['PRIMARYTITLE', 'DIRECTOR', 'CAST', 'GENRES', 'STARTYEAR']
header = netflix_lines[0].split('\t')
index_dict = dict()
netflix_final = []

for key in column_key:
    index_dict[key] = header.index(key)

for line in netflix_lines[1:]:
    netflix_text = line.split('\t')
    netlix_film = {
        'title': netflix_text[index_dict['PRIMARYTITLE']],
        'directors': empty_list(netflix_text[index_dict['DIRECTOR']]),
        'cast': empty_list(netflix_text[index_dict['CAST']]),
        'genres': empty_list(netflix_text[index_dict['GENRES']]),
        'decade': (int(netflix_text[index_dict['STARTYEAR']]) // 10) * 10}
    netflix_final.append(netlix_film)


with open('Voleska_Lucie_HW02_edited.json', mode='w', encoding='utf-8') as output_file:
    json.dump(netflix_final, output_file, ensure_ascii=False, indent=4)


