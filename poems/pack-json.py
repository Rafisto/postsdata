import os

print("Pack-JSON 1.0 RW")

poems = []
titles = []
for file in os.listdir("txt"):
    if file.endswith(".txt"):
        poems.append(os.path.join("txt", file))
        titles.append(file.replace('.txt',''))

json = []

for p in range(len(poems)):
    file = open(poems[p], encoding='utf-8').readlines()
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

for i, poem in enumerate(json):    
    print(f"json/{titles[i]}.json")
    with open(f"json/{titles[i]}.json", "w", encoding="utf-8") as f:
        f.write(str(json).replace("'", '"'))
