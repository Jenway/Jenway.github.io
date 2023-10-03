# !!! this file is deprecated

# the function of it is replace by the javascript file in the script folder
# whicn named generate_random_list.js

# this file is maintained only for a record


# the goal of this script is to create a json file that satisfies :
# we have a img.txt file that contains the iamge link list
# we have a _post folder that contains the markdown files

# make the md have random images, and the images are from the img.txt

import os
import random
import json


def get_img_list(path:str) -> list:
    img_list = []
    with open(path, 'r') as f:
        for line in f.readlines():
            img_list.append(line.strip())
    return img_list


def get_md_list(path:str) -> list:
    def need_cover(file) -> bool:
        # if is a markdown file and has no cover
        if not file.endswith('.md'):
            return False
        with open(file=file, mode='r', encoding='utf-8') as f:
            flag: bool = False
            # 只读取 --- 之间的内容
            for line in f.readlines():
                if line.startswith('---'):
                    if flag:
                        break
                    else:
                        flag = True
                        continue
                if line.startswith('cover:') and line.split(':')[1].strip() != '':
                    return False # if has cover, then no need to add cover
                if line.startswith('hidden:') and line.split(':')[1].strip() == 'true':
                    return False
        return True
    
    md_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if need_cover(os.path.join(root, file)):
                md_name = os.path.join(root, file).replace('\\', '/')
                md_list.append(md_name)
    return md_list

img_path = 'img.txt'
md_path = '_posts'

if __name__ == '__main__':

    img_list = get_img_list(img_path)
    md_list = get_md_list(md_path)

    # create the json file
    result = {}
    cover_add_count = 0
    for md in md_list:
        if len(img_list) == 0:
            print('no more images for' + md + ' !')
        else:
            img_ch = random.choice(img_list)
            img_list.remove(img_ch)
            result[md] = img_ch
            cover_add_count += 1
            print('add: ' + md + ' : ' + img_ch)

    with open('img.json', 'w') as f:
        json.dump(result, f, indent=4)

    print('Add ' + str(len(result)) + ' images to img.json !')
    if len(img_list) != 0:
        print(str(len(img_list)) + ' images left !')
    else:
        print('All images are used !')

    total_md = len(md_list)
    print('Total markdown files: ' + str(total_md))
    print('Add ' + str(cover_add_count) + ' covers !')

    if cover_add_count < total_md:
        print('There are ' + str(total_md - cover_add_count) + ' markdown files that have no cover !')
