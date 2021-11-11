import os
import rename
import sys


# A list of replacements that will standardize the naming of the ThunderHenry repository
thunder_henry_replacements = {
    'THUNDERHENRY': 'ModdedSurvivorCaps',
    'THUNDER HENRY': 'ModdedSurvivorCapsSpace',
    'THUNDER_HENRY': 'ModdedSurvivorCapsUnderscore',
    'THUNDER-HENRY': 'ModdedSurvivorCapsDash',
    'ThunderHenry': 'ModdedSurvivorCamel',
    'Thunder Henry': 'ModdedSurvivorCamelSpace',
    'Thunder_Henry': 'ModdedSurvivorCamelUnderscore',
    'Thunder-Henry': 'ModdedSurvivorCamelDash',
    'thunderhenry': 'ModdedSurvivorLower',
    'thunder henry': 'ModdedSurvivorLowerSpace',
    'thunder_henry': 'ModdedSurvivorLowerUnderscore',
    'thunder-henry': 'ModdedSurvivorLowerDash',

}

henry_replacements = {
    'HENRY': 'ModdedSurvivorCaps',
    'Henry': 'ModdedSurvivorCamel',
    'henry': 'ModdedSurvivorLower',
}


def convert_thunder_henry(directory):
    for original, new in thunder_henry_replacements.items():
        print(f'Step - \n\t{original} -> {new}')
        rename.rename(directory, original, new)
    for original, new in henry_replacements.items():
        print(f'Step - \n\t{original} -> {new}')
        rename.rename(directory, original, new)


if __name__ == '__main__':
    if sys.argv[1].startswith('.'):
        convert_thunder_henry(os.path.join(os.getcwd(), sys.argv[1]))
    else:
        convert_thunder_henry(sys.argv[1])

