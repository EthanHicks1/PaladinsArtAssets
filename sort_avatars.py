import os
import json

path = 'avatars'
list_ = os.listdir(path)
avatar_extensions = {}

for file_ in list_:
    name, ext = os.path.splitext(file_)

    # This is going to store the extension type
    ext = ext[1:]

    avatar_extensions[name] = ext

# print(avatar_extensions)

with open('../cache/avatar_extensions.json', 'w', encoding='utf-8') as f:
    json.dump(avatar_extensions, f, ensure_ascii=False, indent=4)
