import inflection
import os
import shutil
import sys

from analyze import get_guids
from link_survivor import link_survivor
from rename import rename
from rename_survivor import rename_survivor


def create_survivor(unity_project_path, survivor_name):
    """Creates a base Risk of Rain 2 survivor"""
    if not os.path.isdir(unity_project_path):
        raise Exception('Unity project path does not exist')
    print(f'Creating new survivor: {survivor_name}')

    survivor_name = inflection.underscore(survivor_name)

    base_survivor = os.path.join(unity_project_path, 'Assets', 'Survivors', 'ThunderHenry')
    new_survivor = os.path.join(unity_project_path, 'Assets', 'Survivors', inflection.camelize(survivor_name))
    os.mkdir(new_survivor)
    # Walks over all files and folders in the base_survivor folder
    for root, dirs, files in os.walk(base_survivor):
        for folder in dirs:
            base_path = os.path.join(root, folder)
            new_path = base_path.replace(base_survivor, new_survivor)
            if not os.path.isdir(new_path):
                os.mkdir(new_path)

        for file in files:
            # if it is a meta file, skip it
            if file.endswith('.meta'):
                continue

            base_path = os.path.join(root, file)
            new_path = base_path.replace(base_survivor, new_survivor)
            shutil.copy(base_path, new_path)

    rename_henry(new_survivor, survivor_name)

    input('\n\n\n\nPlease open up your project in Unity to generate new .meta files for your new survivor.\n'
          'When Unity is done loading, please close it.\n'
          'Press enter to continue...')

    link_survivor(unity_project_path, survivor_name)

    input('\n\n\n\nPlease open your project in Unity once more to finalize some files that may have been generated.\n'
          'When Unity is done loading, please close it again. (This is the last time this will be needed)\n'
          'Press enter when you are ready to continue...')

    rename_henry(new_survivor, survivor_name)


def rename_henry(survivor_path, survivor_name):
    survivor_name = inflection.underscore(survivor_name)
    if '_' in survivor_name:
        words = survivor_name.split('_')
    else:
        words = [survivor_name]

    thunder_henry_replacements = {
        'THUNDERHENRY': ''.join(word.upper() for word in words),
        'THUNDER HENRY': ' '.join(word.upper() for word in words),
        'THUNDER_HENRY': '_'.join(word.upper() for word in words),
        'THUNDER-HENRY': '-'.join(word.upper() for word in words),
        'ThunderHenry': ''.join(inflection.camelize(word) for word in words),
        'Thunder Henry': ' '.join(inflection.camelize(word) for word in words),
        'Thunder_Henry': '_'.join(inflection.camelize(word) for word in words),
        'Thunder-Henry': '-'.join(inflection.camelize(word) for word in words),
        'thunderhenry': ''.join(word.lower() for word in words),
        'thunder henry': ' '.join(word.lower() for word in words),
        'thunder_henry': '_'.join(word.lower() for word in words),
        'thunder-henry': '-'.join(word.lower() for word in words),
    }

    henry_replacements = {
        'HENRY': ''.join(word.upper() for word in words),
        'Henry': ''.join(inflection.camelize(word) for word in words),
        'henry': ''.join(word.lower() for word in words),
    }
    for henry_name, new_name in thunder_henry_replacements.items():
        rename(survivor_path, henry_name, new_name)

    for henry_name, new_name in henry_replacements.items():
        rename(survivor_path, henry_name, new_name)


if __name__ == '__main__':
    try:
        if len(sys.argv) == 3:
            create_survivor(sys.argv[1], sys.argv[2])
        else:
            raise Exception('Usage: ./create_survivor.py <unity_project_path> <survivor_name>')
    except Exception as e:
        print(e)
    input('\n\n\n\nPress enter to exit...')

