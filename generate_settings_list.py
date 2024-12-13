from config.definitions import ROOT_DIR
import os

apply_dark = []
settings_list = []

try:
    with open(os.path.join(ROOT_DIR, 'apply_dark.txt'), 'r') as file:
        for line in file:
            apply_dark.append(line.strip())
except Exception as e:
    print(e)

for setting in apply_dark:
    temp = setting.split(' ')
    settings_list.append(temp[0])

try:
    with open(os.path.join(ROOT_DIR, 'settings_list.txt'), 'w') as file:
        for line in settings_list:
            file.write(line + '\n')
except Exception as e:
    print(e)

print('done')