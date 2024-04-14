import autopep8
import chardet

def fix_indentation(file_path):
    try:
        with open(file_path, 'rb') as file:
            rawdata = file.read()
            result = chardet.detect(rawdata)
            charenc = result['encoding']

        with open(file_path, 'r', encoding=charenc) as file:
            code = file.read()

        fixed_code = autopep8.fix_code(code)

        with open(file_path, 'w', encoding=charenc) as file:
            file.write(fixed_code)
    except FileNotFoundError:
        print(f"Error: No such file or directory: '{file_path}'")

# Usage
fix_indentation('test.py')