import os

print("--Gallery-Rename-Pack-Json 1.0 RW\n___\n")

json = []
print("--Posts Path Traversal:")
for i, dir in enumerate(os.listdir("gallery/")):
    if '.json' not in dir:
        print('gallery/'+str(i)+'.jpg')
        os.rename('gallery/'+dir, 'gallery/'+str(i)+'.jpg')
        json.append(str(i)+'.jpg')

with open("gallery/__list__.json", "w", encoding="utf-8") as f:
    print("gallery/__list__.json")
    f.write(str(json).replace("'", '"'))