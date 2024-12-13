from config.definitions import ROOT_DIR
import os

def revert_to_default():
    open_success = False
    to_remove = []
    editor_settings = []
    editor_settings_reverted = []

    try:
        with open(os.path.join(ROOT_DIR, 'differences.txt'), 'r') as file:
            for line in file:
                to_remove.append(line)
    except Exception as e:
        print(e)

    editor_setting_path = input('enter path to Godot editor settings file: ').strip()
    try:
        with open(editor_setting_path, 'r') as file:
            for lines in file:
                editor_settings.append(lines)
        open_success = True
        print('path found')
    except Exception as e:
        print("Couldn't open settings file, please check if path is correct")
    
    # checks each line in the current settings file
    # if the line is in the settings we set for custom theme
    # don't append them to list, if they aren't then append them to list
    # use the list to create a new settings file

    i = 0
    for lines in editor_settings:
        removed = False
        for l in to_remove:
            if l.strip() in lines:
                i += 1
                removed = True
        if not removed:
            editor_settings_reverted.append(lines)
        #if 'interface/theme/base_color' in lines:
            #editor_settings_reverted.append(base_color_insert)
        #elif 'interface/theme/accent_color' in lines:
            #editor_settings_reverted.append(accent_color_insert)
    print('new file settings created, removed ' + str(i) + ' lines')
    
    try:
        with open(editor_setting_path, 'w') as file:
            for lines in editor_settings_reverted:
                file.write(lines)
        print('reverted')
    except Exception as e:
        print(e)

    input()

def revert_to_previous():
    print('reverting theme settings to previous')

    to_remove = []
    editor_settings = []
    editor_settings_reverted = []
    last_settings = []

    try:
        with open(os.path.join(ROOT_DIR, 'differences.txt'), 'r') as file:
            for line in file:
                to_remove.append(line.strip())
    except Exception as e:
        print(e)

    try:
        with open(os.path.join(ROOT_DIR, 'backup_settings.txt'), 'r') as file:
            for line in file:
                last_settings.append(line.strip())
    except Exception as e:
        print('could not find backup_settings.txt')


    editor_setting_path = input('enter path to Godot editor settings file: ').strip()
    try:
        with open(editor_setting_path, 'r') as file:
            for lines in file:
                editor_settings.append(lines.strip())
        print('path found')
    except Exception as e:
        print("Couldn't open settings file, please check if path is correct")
    
    # checks each line in the current settings file
    # if the line is in the settings we set for custom theme
    # don't append them to list, if they aren't then append them to list
    # use the list to create a new settings file

    for lines in editor_settings:
        removed = False
        for l in to_remove:
            if l in lines:
                removed = True
                break
        if not removed:
            editor_settings_reverted.append(lines)
            print(lines)
    
    i = 0
    for lines in editor_settings_reverted:
        if lines == '[resource]':
            for setting in last_settings:
                i += 1
                editor_settings_reverted.insert(i, setting)
        i += 1
    
    try:
        with open(editor_setting_path, 'w') as file:
            for lines in editor_settings_reverted:
                file.write(lines + '\n')
        print('reverted theme settings to previous theme')
    except Exception as e:
        print(e)

    input()

def apply_theme():
    settings_to_apply = []
    editor_settings = []
    settings_list = []
    final_settings = []
    backup_settings = []

    try:
        with open(os.path.join(ROOT_DIR, 'apply_dark.txt'), 'r') as file:
            for line in file:
                settings_to_apply.append(line.strip())
    except Exception as e:
        print(e)

    try:
        with open(os.path.join(ROOT_DIR, 'settings_list.txt'), 'r') as file:
            for line in file:
                settings_list.append(line.strip())
    except Exception as e:
        print(e)

    editor_setting_path = input('enter path to Godot editor settings file: ').strip()
    try:
        with open(editor_setting_path, 'r') as file:
            for lines in file:
                editor_settings.append(lines.strip())
                for setting in settings_list:
                    if setting in lines:
                        backup_settings.append(lines.strip())
        open_success = True
        print('path found')
    except Exception as e:
        print("Couldn't open settings file, please check if path is correct")

    try:
        with open(os.path.join(ROOT_DIR, 'backup_settings.txt'), 'w') as file:
            for line in backup_settings:
                file.write(line + '\n')
    except Exception as e:
        print('error creating backup settings file: ' + e)
    
    i = 0
    for line in editor_settings:
        not_found = True
        if line != '[resource]':
            for setting in settings_list:
                if setting in line:
                    not_found = False
                    break
            if not_found:
                final_settings.append(line)
        else:
            final_settings.append(line)
            for setting in settings_to_apply:
                final_settings.append(setting)
                #if 'interface/theme/preset' in setting:
                    #final_settings.append('interface/theme/custom_theme = "' + theme_path + '"')

    try:
        with open(editor_setting_path, 'w') as file:
            for setting in final_settings:
                file.write(setting + '\n')
    except Exception as e:
        print(e)

    print('new settings file created')

    

def main():
    good = False
    while not good:
        print('type "revert-default" to revert theme to default')
        print('type "revert-previous" to revert theme to default')
        print("the revert options will not overwrite any non-theme settings you've changed")
        print('type "apply theme" to apply theme')
        command_in = input(': ')

        if 'revert-default' in command_in:
            good = True
            revert_to_default()
        elif 'apply theme' in command_in:
            good = True
            apply_theme()
        elif 'exit' in command_in:
            good = True
        elif 'previous' in command_in:
            revert_to_previous()
            good = True
        else:
            print('command not recognized, please enter a valid command\n')

if __name__ == "__main__":
    main()