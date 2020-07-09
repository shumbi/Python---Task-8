import json
from collections import Counter

with open("newsafr.json", encoding='utf-8') as file:
    json = json.load(file)

word_list = []
for a in json["rss"]["channel"]["items"]:
    article_t = a["description"]
    article_s = article_t.split()
    for w in article_s:
        if len(w) > 6:
            word_list.append(w)
print('Список слов топ-10 из новостей: ', Counter(word_list).most_common(10))


