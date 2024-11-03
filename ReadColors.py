'''
Carlo Baltao

ADEV-3005 (254275)

Topic Challenge - Module 6A
'''

color_names = 'colors.txt'

def create_file(file_name):
    """
    Writes content to file name.
    """
    with open(file_name, 'w') as colors:
        colors.write("Amethyst #9966cc\nApricot #fbceb1\nAqua #00ffff\nBlond #faf0be")

def read_and_replace(file_name):
    """
    Reads the file passed to the function line by line, finds the word 'Aqua', replaces the whole line, 
    and adds the line to the new modified lines list.
    If 'Aqua' is not found, the original line is appended to the new modified lines list.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()

    modified_lines = []

    for line in lines:
        modified_lines.append(line.replace("Aqua #00ffff", "Azure #007fff"))
    
    return modified_lines

def overwrite_file(file_name, new_content):
    """
    Overwrites the file being passed to the function with the content being passed to the function.
    """
    with open(file_name, 'w') as file:
        file.writelines(new_content)

create_file(color_names)

with open(color_names, 'r') as file:
    print("\nOriginal File Content:\n" + file.read())

modified_lines = read_and_replace(color_names)
overwrite_file(color_names, modified_lines)

with open(color_names, 'r') as file:
    print("\nNew File Content: \n" + file.read())

