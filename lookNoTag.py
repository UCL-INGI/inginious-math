# Author: Victor Belpaire
# Date: 09-07-2020
#
# This script look after INGInious exercices without tags.
# /!\ Change directory before run (@dir)


import pathlib

dir = "Maxime"
count = 0
count2 = 0

for path in pathlib.Path(dir).iterdir():
    if path.is_dir():
        try:
            file = open(str(path)+"/task.yaml", 'r')
            lines = file.readlines()
            file.close()
            if 'categories: []' in lines:
                print(str(path), "has no tags !!!")
                count += 1
            else:
                i = lines.index('categories:\n')
                print(str(path), "has tags: ", end="")
                j = 1
                while(lines[i+j] != "contact_url: ''\n"):
                    print(lines[i+j][2:-1], end=", ")
                    j += 1
                print()

            count2 += 1
        except:
            continue

print()
if count == 0:
    print('Every exercice has tags')
else:
    print('There is {} exercices without tags'.format(count))
print('There is {} exercices'.format(count2))
