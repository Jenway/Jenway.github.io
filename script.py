# the goal of this script is to create a json file that satisfies :
# we have a img.txt file that contains the iamge link list
# we have a _post folder that contains the markdown files

# make the md have random images, and the images are from the img.txt

import os
import random
import json


def if_exist_cover(md):
    with open(md, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if line.startswith('cover:') and line.strip() != 'cover:':
                return True
    return False

# remote_link = 'https://cdn.statically.io/gh/Jenway/J-figure-Bed/main/img.txt'
remote_link = 'https://raw.githubusercontent.com/Jenway/J-figure-Bed/main/img.txt'

# download the img.txt
os.system('curl -o img.txt ' + remote_link)

# get the image list
img_list = []
with open('img.txt', 'r') as f:
    for line in f.readlines():
        img_list.append(line.strip())

# get the md list
md_list = []
for root, dirs, files in os.walk('_posts'):
    for file in files:
        if file.endswith('.md') and not if_exist_cover(os.path.join(root, file)):
            md_name = os.path.join(root, file).replace('\\', '/')
            md_list.append(md_name)

# create the json file
result = {}
for md in md_list:
    if len(img_list) == 0:
        break
    img_ch = random.choice(img_list)
    img_list.remove(img_ch)
    result[md] = img_ch

with open('img.json', 'w') as f:
    json.dump(result, f, indent=4)

print('done')