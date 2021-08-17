
import fileinput
import os
import re

def get_max_and_ultimate_skill_level(path_to_file):
    max_level = 0
    ult_level = 0
    path_to_file = path_to_file.replace('\\', '/')
    fp = open(path_to_file, 'r')
    lines = fp.readlines()
    fp.close()
    for index, line in enumerate(lines):
        sub_lines = line.split(',')
        # Parameter name
        param_name = sub_lines[0]
        # Parameter value
        param_value = sub_lines[1]
        if param_name == 'skillMaxLevel':
            max_level = param_value
        if param_name == 'skillUltimateLevel':
            ult_level = param_value
    return max_level, ult_level

def set_max_and_ultimate_skill_level(path_to_file, needed_max_level, needed_ult_level, needed_mastery_level):
    cur_max_level, cur_ult_level = get_max_and_ultimate_skill_level(path_to_file)
    # If this is a regular skill, not mastery
    if 'mastery.dbr' not in path_to_file:
        for f_line in fileinput.input([path_to_file], inplace=True):
            print(f_line.replace('skillUltimateLevel,'+str(cur_ult_level),
                                 'skillUltimateLevel,'+str(needed_ult_level)).replace('skillMaxLevel,' + str(cur_max_level),
                                                                                  'skillMaxLevel,' + str(needed_max_level)), end='')
    # Mastery does not have skillUltimateLevel, so ignore it
    else:
        for f_line in fileinput.input([path_to_file], inplace=True):
            print(f_line.replace('skillMaxLevel,' + str(cur_max_level), 'skillMaxLevel,' + str(needed_mastery_level)), end='')

def increase_skills_to_needed_levels(path_to_file, needed_ult_level):
    # This is a lazy shitty function
    def process_single_value(p_name, p_value, max_level, line):
        new_val = p_value
        param_values = str(new_val).split(';')
        #param_values.append(new_val)
        val_deviation = 2
        for r in range(len(param_values), max_level):
            s_new_val = str(str(new_val).split('.')[0]) + '.000000'
            if type(new_val) is int:
                new_val = int(new_val) + val_deviation
                s_new_val = new_val
            elif type(new_val) is float:
                new_val = float(new_val) + val_deviation
                s_new_val = str(str(new_val).split('.')[0]) + '.000000'
            param_values.append(s_new_val)
        new_line = ''
        for val in param_values:
            if len(new_line) != 0:
                new_line += ';' + str(val)
            else:
                new_line = str(val)
        new_line = p_name + ',' + new_line + ',\n'
        if new_line != '':
            for f_line in fileinput.input([path_to_file], inplace=True):
                print(f_line.replace(line, new_line), end='')

    fp = open(path_to_file, 'r')
    lines = fp.readlines()
    fp.close()
    pattern = re.compile("[A-Za-z]+")
    for index, line in enumerate(lines):
        sub_lines = line.split(',')
        # Parameter name
        param_name = sub_lines[0]
        # Parameter value
        param_value = sub_lines[1]
        if '\\' not in param_value and pattern.fullmatch(param_value) is None:
            # Work with parameters with multiple values
            if ';' in param_value:
                # Get values
                param_values = param_value.split(';')
                # Get last and penultimate values
                try:
                    last_val = float(param_values[-1])
                    pre_last_val = float(param_values[-2])
                # Simple go to next step of loop
                except Exception as e:
                    continue
                # Get deviation between last and penultimate values
                deviation = last_val - pre_last_val
                # Make new values for increased level of skill
                for i in range(len(param_values), needed_ult_level):
                    if param_name != 'skillManaCost':
                        last_val = last_val + deviation + last_val/100
                    else:
                        last_val = last_val + deviation + 1
                    s_last_val = str(str(last_val).split('.')[0]) + '.000000'
                    # Append value
                    param_values.append(s_last_val)
                new_line = ''
                # Make new line with new values
                for val in param_values:
                    if len(new_line) != 0:
                        new_line += ';' + val
                    else:
                        new_line = val
                # Add parameter name to new line
                new_line = param_name + ',' + new_line + ',\n'
                if new_line != '':
                    # And replace old line values with new line
                    for f_line in fileinput.input([path_to_file], inplace=True):
                        print(f_line.replace(line, new_line), end='')
            # Lets work with some single-valued parameters
            else:
                if param_name == 'skillActiveManaCost' or param_name == 'skillActiveLifeCost' or param_name == 'skillManaCost' or param_name == 'skillActiveDuration':
                    try:
                        fake_param = int(param_value) + 1 - 1
                    except ValueError:
                        try:
                            fake_param = float(param_value) + 1.00 - 1.00
                        # Strings...
                        except ValueError:
                            continue
                        else:
                            param_value = fake_param
                            # Нужно добавить обработку конкретных одиночных значений
                            if param_value != 0:
                                process_single_value(param_name, param_value, needed_ult_level, line)
                    else:
                        param_value = fake_param
                        # Нужно добавить обработку конкретных одиночных значений
                        if param_value != 0:
                            process_single_value(param_name, param_value, needed_ult_level, line)

def check_paths(dir_paths):
    result = ''
    paths = dir_paths.split(';')
    for dir_path in paths:
        if not os.path.exists(dir_path):
            result = dir_path
            break
    return result

def ask_user_for_input():
    # Skills directory
    while True:
        path_to_skills_dir = input("Enter one or more path to the folder with .dbr files with skills (raw path without quotes; if multiple then delimited with ';'): ")
        check_status = check_paths(path_to_skills_dir)
        if check_status != '':
            print("Sorry, provided path does not exists: " + check_status)
            continue
        else:
            print('Your path\paths is: ' + path_to_skills_dir)
            break
    # Desired max level of skills
    while True:
        try:
            need_skill_max_level = int(input("Enter desired max level of skills (only integer numbers allowed): "))
        except ValueError:
            print("Sorry, provided value is not integer.")
            continue
        else:
            print('Your max level of skills is: ' + str(need_skill_max_level))
            break
    # Desired ultimate level of skills
    while True:
        try:
            need_skill_ult_level = int(input("Enter desired ultimate level of skills (only integer numbers allowed, and must be greater-or-equal then max level): "))
            if need_skill_ult_level < need_skill_max_level:
                # Raise exception in a weird way
                need_skill_max_level = need_skill_max_level / 0
        except Exception:
            print("Sorry, provided value is not integer, or lesser then max level of skills")
            continue
        else:
            print('Your ultimate level of skills is: ' + str(need_skill_ult_level))
            break
    # Desired max level of masteries
    while True:
        try:
            need_mastery_level = int(input("Enter desired masteries level (only integer numbers allowed, and must be greater-or-equal then ultimate level): "))
            if need_mastery_level < need_skill_ult_level:
                # Raise exception in a weird way
                need_skill_max_level = need_skill_max_level / 0
        except Exception:
            print("Sorry, provided value is not integer, or lesser then max level of skills")
            continue
        else:
            print('Your mastery level is: ' + str(need_mastery_level))
            break
    return path_to_skills_dir, need_skill_max_level, need_skill_ult_level, need_mastery_level

##################################################################
##################################################################
##################################################################


_PATH_TO_SKILLS, _NEED_SKILL_MAX_LEVEL, _NEED_ULT_LEVEL, _NEED_MASTERY_MAX_LEVEL = ask_user_for_input()
_PATHS = _PATH_TO_SKILLS.split(';')
for _PATH in _PATHS:
    for path, subdirs, files in os.walk(_PATH):
        for name in files:
            file_path = os.path.join(path, name)
            set_max_and_ultimate_skill_level(file_path, _NEED_SKILL_MAX_LEVEL, _NEED_ULT_LEVEL, _NEED_MASTERY_MAX_LEVEL)
            increase_skills_to_needed_levels(file_path, _NEED_ULT_LEVEL)
