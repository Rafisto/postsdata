import os

print("___\nPoems-Pack-JSON 1.1 RW\n___\n")

poems = []
titles = []
for file in os.listdir("poems/txt"):
    if file.endswith(".txt"):
        poems.append(os.path.join("txt", file))
        titles.append(file.replace('.txt', ''))

json = []
data = []

for p in range(len(poems)):
    file = open("poems/"+poems[p], encoding='utf-8').readlines()
    poem_dict = {}
    text = []
    poem_dict["url"] = poems[p].split('\\')[1].split('.')[0]
    poem_dict["id"] = p + 1
    for i in range(len(file)):
        if i == 0:
            poem_dict["date"] = file[i][:-1]
        elif i == 1:
            poem_dict["title"] = file[i][:-1]
        elif i == 2:
            poem_dict["description"] = file[i][:-1]
        else:
            text.append(file[i][:-1])
    poem_dict["content"] = text
    json.append(poem_dict)
    dicts = poem_dict.copy()
    dicts.pop("content")
    data.append(dicts)

with open("poems/__list__.json", "w", encoding="utf-8") as f:
    print("poems/__list__.json")
    f.write(str(data).replace("'", '"'))

for i, poem in enumerate(json):
    print(f"poems/json/{titles[i]}.json")
    with open(f"poems/json/{titles[i]}.json", "w", encoding="utf-8") as f:
        f.write(str(poem).replace("'", '"'))
