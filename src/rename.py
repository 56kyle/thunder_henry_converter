
import sys
import os


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
                    try:
                        os.remove(original_file)
                    except Exception as e:
                        print(f'\t\tError: {e}')
                else:
                    if original_name in original_file:
                        print(f'Renaming original file - {original_file}')
                        os.rename(original_file, new_file)
                        print(f'\t{new_file}')
                    try:
                        # replace all occurrences of the original name inside of the file with the new name
                        with open(new_file, 'r') as f:
                            content = f.read()
                        with open(new_file, 'w') as f:
                            if content.replace(original_name, new_name) != content:
                                print(f'Modifying File - {new_file}')
                            f.write(content.replace(original_name, new_name))
                    except Exception as e:
                        print(f'\t\tError: {e}')
            except Exception as e:
                print(f'\tError: {e}')

        for folder in dirs:
            try:
                if original_name in folder:
                    os.rename(os.path.join(root, folder), os.path.join(root, folder.replace(original_name, new_name)))
                    print(f'Renaming original folder - {os.path.join(root, folder)}')
                    print(f'\t{os.path.join(root, folder.replace(original_name, new_name))}')
            except Exception as e:
                print(f'\tError: {e}')


# have it so that typing "python rename.py foo bar baz" will call rename(os.path.join(os.getcwd(), "foo"), "bar", "baz")
if __name__ == "__main__":
    if len(sys.argv) == 4:
        rename(os.path.join(os.getcwd(), sys.argv[1]), sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        rename(os.getcwd(), sys.argv[1], sys.argv[2])

    input('Press enter to exit')


