from pathlib import Path

import sys
class Tree:
    def __init__(self, directory, save_location):
        assert isinstance(directory, Path), 'Not a Path object'
        assert isinstance(save_location, Path), 'Not a Path object'

        self.directory = directory
        self.directory_name = self.directory.parts[-1]
        self.save_location = save_location

        ## Changeable ##
        self.text_name = 'tree.txt'
        self.spaces = 2
        self.file_format = '- '
        self.folder_format = '+ '
        ################

        self.generate_tree()

    def generate_tree(self):
        with open(str(Path.joinpath(self.save_location, self.text_name)), 'w', encoding='UTF-8') as f:
            f.write('Tree Diagram for \'{}\' path.\n\n'.format(self.directory))
            f.write('{}{}{}'.format(self.folder_format, self.directory_name, '\n'))

            f.write(self.recursive_generate_tree(self.directory))

    def recursive_generate_tree(self, folder_path):
        tree = ''
        for path in Path(folder_path).glob('*'):
            tree += self.generate_line(path)
            if path.is_dir():
                tree += self.recursive_generate_tree(path)
        return tree
    
    def generate_line(self, path):
        path_relative = path.relative_to(self.directory)
        number = len(path_relative.parts)
        if path.is_dir():
            return (len(self.folder_format) + self.spaces * number) * ' ' + self.folder_format + str(path_relative.parts[-1]) + '\n'
        else:
            return (len(self.folder_format) + self.spaces * number) * ' ' + self.file_format + str(path_relative.parts[-1]) + '\n'
