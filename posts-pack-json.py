import os

print("--Posts-Pack-JSON 1.0 RW\n___\n")

posts = []
titles = []
print("--Posts Path Traversal:")
for dir in os.listdir("posts/"):
    if '.json' not in dir:
        for file in os.listdir("posts/"+dir):
            print(dir)
            if file.endswith(".md"):
                posts.append(os.path.join(dir, file))
                titles.append(file)

json = []
data = []

for p in range(len(posts)):
    print("--Posts Json Generation")
    file = open("posts/"+posts[p], encoding='utf-8').readlines()
    post_dict = {}
    post_dict["url"] = titles[p].replace('.md','')
    post_dict["id"] = p + 1
    for i in range(len(file)):
        if i == 0:
            post_dict["title"] = file[i][:-1].replace('### ','')
        elif i == 1:
            post_dict["date"] = file[i][:-1]
        elif i == 2:
            post_dict["description"] = file[i][:-1]
    text = ''.join(file)
    post_dict["content"] = text
    json.append(post_dict)
    dicts = post_dict.copy()
    dicts.pop("content")
    data.append(dicts)

with open("posts/__list__.json", "w", encoding="utf-8") as f:
    print("--Save posts/__list__.json")
    f.write(str(data).replace("'", '"'))

print("--Save json")
for i, post in enumerate(json):
    title = titles[i].replace('.md','')
    print(f"--Save posts/json/{title}.json")
    with open(f"posts/json/{title}.json", "w", encoding="utf-8") as f:
        f.write(str(post).replace("'", '"'))
