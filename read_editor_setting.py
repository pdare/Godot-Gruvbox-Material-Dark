default_settings = []
altered_settings = []
difference = []

try:
    with open('default_editor_settings-4.4.tres', 'r') as file:
        for line in file:
            default_settings.append(line)
except Exception as e:
    print(e)

try:
    with open('changed_editor_settings-4.4.tres', 'r') as file:
        for line in file:
            altered_settings.append(line)
except Exception as e:
    print(e)


for line in altered_settings:
    found = False
    for l in default_settings:
        if line == l:
            found = True
            break
    if not found:
        temp = line.split(' ')
        difference.append(temp[0] + '\n')

try:
    with open('differences.txt', 'w') as file:
        for l in difference:
            file.write(l)
except Exception as e:
    print(e)



input()