
import json
import os
import sys
import yaml

paths = {}

def get_guids(base_path):
    # walk over all files and folders in the directory
    for root, dirs, files in os.walk(base_path):
        for file in files:
            path = os.path.join(root, file)
            if 'stage' in path:
                print(path)
            if file.endswith('.meta'):
                # skip meta files
                continue
            guid = get_meta_info(path)
            paths[path] = guid

        for folder in dirs:
            path = os.path.join(root, folder)
            guid = get_meta_info(path)
            paths[path] = guid
    return paths


def get_meta_info(path):
    try:
        meta_path = path + '.meta'
        if os.path.isfile(meta_path):
            # read the meta file as a yaml file
            with open(meta_path, 'r') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                guid = data['guid']
                return guid
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_guids(sys.argv[1])
    else:
        raise Exception('Invalid number of arguments')
    input('Press enter to leave')

