import json
import os
import sys


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
        return json.loads(data, encoding='utf-8')
    except FileNotFoundError as e1:
        raise Exception(f"File {filename} does not exists")
    except json.decoder.JSONDecodeError as e2:
        raise Exception(f"File {filename} is not a json file")


def nbmerge(files):
    if len(files) < 3:
        raise Exception("Command format: nbmerge file1.ipynb file2.ipynb ...")

    print(f"Number of files: {len(files)}")

    if len([i for i in files if '.ipynb' in i]) != len(files):
        raise Exception("Ensure all input files end with .ipynb")

    print("Metadata of the first file will be kept, cells "
          "of other files will be appended to that of the first file")

    output_data = read_file(files[0]).copy()
    print(f"Cells: {len(output_data['cells'])} : {files[0]}")

    for i in files[1:]:
        data = read_file(i)['cells']
        print(f"Cells: {len(data)} : {i}")
        output_data['cells'] += data

    print(f"All files merged: Total cells: {len(output_data['cells'])}\n")

    output_file_name = input("Enter output file name (without .ipynb) WILL BE OVERWRITTEN: ") + ".ipynb"

    with open(output_file_name, 'w', encoding='utf-8') as output:
        output.write(json.dumps(output_data, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    nbmerge(sys.argv[1:])
