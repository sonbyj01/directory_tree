#!/usr/bin/env
from pathlib import Path
import sys

from tree import Tree

def main():
    directory = input('Enter absolute path of directory: ')
    save_location = input('Enter absolute path of where you want to save text file: ')

    if Path(directory).is_absolute():
        directory_path = Path(directory)
    # else:
    #     directory_path = Path.joinpath(Path.cwd(), Path(directory)).resolve()

    if Path(save_location).is_absolute():
        save_location_path = Path(save_location)
    # else:
    #     save_location_path = Path.joinpath(Path.cwd(), Path(save_location)).resolve()
    
    # print(directory_path)
    # print(save_location_path)
    # sys.exit()
    Tree(directory_path, save_location_path)

if __name__ == "__main__":
    main()
