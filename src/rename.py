
import sys
import os

"""A script that is used to replace all instances of a word in folder names, file names, and inside of files"""

# Walk over all folders and files at the provided path
# and rename all folders and files so that any occurrence
# of the original name in the name is replaced with the new name
def rename(path, original_name, new_name):
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                original_file = os.path.join(root, file)
                new_file = os.path.join(root, file.replace(original_name, new_name))

                # if the file name ends with .meta, then delete the file
                if original_file.endswith('.meta'):
                    pass
                else:
                    if original_name in original_file:
                        os.rename(original_file, new_file)
                        print(f'Renaming original file - {original_file}')
                        print(f'\t{new_file}')

                        take_care_of_meta_file(original_file, new_file)

                    try:
                        # replace all occurrences of the original name inside of the file with the new name
                        with open(new_file, 'r') as f:
                            content = f.read()
                        with open(new_file, 'w') as f:
                            if content.replace(original_name, new_name) != content:
                                print(f'Modifying File - {new_file}')
                            f.write(content.replace(original_name, new_name))
                    except Exception as e:
                        pass
                        #print(f'\t\tError: {e}')
            except Exception as e:
                pass
                #print(f'\tError: {e}')

        for folder in dirs:
            original_folder = os.path.join(root, folder)
            new_folder = os.path.join(root, folder.replace(original_name, new_name))
            try:
                if original_name in folder:
                    os.rename(original_folder, new_folder)
                    print(f'Renaming original folder - {original_folder}')
                    print(f'\t{new_folder}')

                    take_care_of_meta_file(original_folder, new_folder)

            except Exception as e:
                print(f'\tError: {e}')


# renames the original_file + '.meta' to the new_file + '.meta'
def take_care_of_meta_file(original_file, new_file):
    try:
        original_meta_file = original_file + '.meta'
        new_meta_file = new_file + '.meta'
        os.rename(original_meta_file, new_meta_file)
        print(f'Renaming original meta file - {original_meta_file}')
        print(f'\t{new_meta_file}')
    except Exception as e:
        print(f'\tError: {e}')


# have it so that typing "python rename.py foo bar baz" will call rename(os.path.join(os.getcwd(), "foo"), "bar", "baz")
if __name__ == "__main__":
    if len(sys.argv) == 4:
        rename(os.path.join(os.getcwd(), sys.argv[1]), sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        rename(os.getcwd(), sys.argv[1], sys.argv[2])

    input('Press enter to exit')


