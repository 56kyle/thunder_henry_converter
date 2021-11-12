import inflection
import json
import os
import sys

from analyze import get_guids


# updates all instances of the original guid references from original_paths.json with the newly generated guids
def link_survivor(unity_project_path, survivor_name):
    if not os.path.isdir(unity_project_path):
        raise Exception('Unity project path does not exist')
    survivor_name = inflection.underscore(survivor_name)

    new_survivor_folder = os.path.join(unity_project_path, 'Assets', 'Survivors', inflection.camelize(survivor_name))
    new_guids = get_guids(new_survivor_folder)

    old_survivor_folder = os.path.join(unity_project_path, 'Assets', 'Survivors', 'ModdedSurvivorCamel')
    old_guids = get_guids(old_survivor_folder)

    # walk over all files and folders in the survivor folder
    for root, dirs, files in os.walk(new_survivor_folder):
        for file in files:
            # if it is a meta file, skip it
            if file.endswith('.meta'):
                continue

            # open the file and replace any old guids with the new guids
            new_path = os.path.join(root, file)

            try:
                with open(new_path, 'r') as new_file:
                    content = new_file.read()

                new_content = content
                for guid_old_path, old_guid in old_guids.items():
                    guid_new_path = guid_old_path.replace(old_survivor_folder, new_survivor_folder)
                    new_guid = new_guids[guid_new_path]
                    new_content = new_content.replace(old_guid, new_guid)

                with open(new_path, 'w') as new_file:
                    new_file.write(new_content)
            except Exception as e:
                print(f'Error updating {new_path}: {e}')

    add_to_editor(unity_project_path, survivor_name)


def add_to_editor(unity_project_path, survivor_name):
    if not os.path.isdir(unity_project_path):
        raise Exception('Unity project path does not exist')
    editor_asmdef = os.path.join(unity_project_path, 'Assets', 'Editor', 'EditorAssembly.asmdef')
    # open editor_asmdef as a json file
    with open(editor_asmdef, 'r') as editor_file:
        data = json.load(editor_file)

    if inflection.camelize(survivor_name) not in data['references']:
        data['references'].append(inflection.camelize(survivor_name))
        with open(editor_asmdef, 'w') as editor_file:
            json.dump(data, editor_file, indent=4)


if __name__ == '__main__':
    try:
        if len(sys.argv) == 3:
            link_survivor(sys.argv[1], sys.argv[2])
        else:
            raise Exception('Usage: link_survivor.py <unity_project_path> <survivor_name>')
    except Exception as e:
        print(e)
    input('\n\n\n\nPress enter to exit...')
