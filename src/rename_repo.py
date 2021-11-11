
import convert_thunder_henry
import inflection
import os
import rename
import sys

"""A script used to replace ModdedSurvivor with the correct version of a name that is provided as input"""

thunder_henry_replacements = {
    'ModdedSurvivorCaps': None,
    'ModdedSurvivorCapsSpace': None,
    'ModdedSurvivorCapsUnderscore': None,
    'ModdedSurvivorCapsDash': None,
    'ModdedSurvivorCamel': None,
    'ModdedSurvivorCamelSpace': None,
    'ModdedSurvivorCamelUnderscore': None,
    'ModdedSurvivorCamelDash': None,
    'ModdedSurvivorLower': None,
    'ModdedSurvivorLowerSpace': None,
    'ModdedSurvivorLowerUnderscore': None,
    'ModdedSurvivorLowerDash': None,
}


def rename_repo(dir_path, new_name):
    for original_name in thunder_henry_replacements.keys():
        print(original_name)
        if '_' in new_name:
            words = new_name.split('_')
        else:
            words = [new_name]

        try:
            if original_name.endswith('Caps') or original_name.endswith('CapsSpace') or original_name.endswith(
                    'CapsUnderscore') or original_name.endswith('CapsDash'):
                words = [word.upper() for word in words]
            if original_name.endswith('Camel') or original_name.endswith('CamelSpace') or original_name.endswith(
                    'CamelUnderscore') or original_name.endswith('CamelDash'):
                words = [inflection.camelize(word) for word in words]
            if original_name.endswith('Lower') or original_name.endswith('LowerSpace') or original_name.endswith(
                    'LowerUnderscore') or original_name.endswith('LowerDash'):
                words = [word.lower() for word in words]
        except Exception as e:
            print(e)

        new_altered_name = new_name
        if len(words) > 1:
            try:
                if original_name.endswith('Caps') or original_name.endswith('Lower'):
                    new_altered_name = ''.join(words)
                elif original_name.endswith('Space'):
                    new_altered_name = ' '.join(words)
                elif original_name.endswith('Underscore'):
                    new_altered_name = '_'.join(words)
                elif original_name.endswith('Dash'):
                    new_altered_name = '-'.join(words)
                else:
                    print('Error: Unknown name type: ' + original_name)
                    continue
            except Exception as e:
                print(e)
        else:
            new_altered_name = words[0]
        thunder_henry_replacements[original_name] = new_altered_name
    for k, v in thunder_henry_replacements.items():
        print(f'{k} -> {v}')

    for k, v in thunder_henry_replacements.items():
        rename.rename(dir_path, k, v)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        rename_repo(os.getcwd(), sys.argv[1])

    elif len(sys.argv) == 3:
        if sys.argv[1].startswith('.'):
            rename_repo(os.path.join(os.getcwd(), sys.argv[1]), sys.argv[2])
        else:
            rename_repo(sys.argv[1], sys.argv[2])

    input('Press enter to leave')
