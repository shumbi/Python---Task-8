import xml.etree.ElementTree as ET
from collections import Counter

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

temp_list = root.findall("channel/item/description")

final_list = []
for a in temp_list:
    article_s = a.text.split()
    for w in range(len(article_s)):
        if len(article_s[w]) > 6:
            final_list.append(article_s[w])
print('Список слов топ-10 из новостей: ', Counter(final_list).most_common(10))