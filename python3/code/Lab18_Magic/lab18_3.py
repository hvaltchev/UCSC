#!/usr/bin/env python3
"""lab18_3.py tree command in python"""
import os, sys

class Node:
    too_many_slashes = None
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.slashes = self.dir_name.count(os.sep)
        self.root_dir = False
        if self.too_many_slashes == None: # first directory
            Node.too_many_slashes = self.slashes - 1
            self.slashes = 0
            self.root_dir = True
    def __str__(self):
        return "   |" * self.slashes + "---" if not self.root_dir else ''

class FileNode(Node):
    first_dir = True
    def __init__(self, dir_node, file_name):
        Node.__init__(self, dir_node.dir_name)
        self.path = os.path.join(dir_node.dir_name, file_name)
        self.name = file_name
        if FileNode.first_dir:
            FileNode.first_dir = False
        self.slashes -= self.too_many_slashes

    def __str__(self):
        return Node.__str__(self) + self.name

class DirNode(Node):
    def __init__(self, dir_name):
        Node.__init__(self, dir_name)
        self.file_nodes = []
        self.slashes -= self.too_many_slashes + 1
        
    def AddFileNode(self, file_node):
        self.file_nodes += [file_node]

    def __str__(self):
        return_str = Node.__str__(self) + self.dir_name + os.sep
        files_part = '\n'.join(str(f) for f in self.file_nodes) 
        if self.file_nodes:
            return return_str + '\n'  + files_part
        return return_str
    
class Tree:
    def __init__(self, start_at):
        self.dir_nodes = []
        def IsGood(file_name):
            BAD_ENDERS = '#', '~', "pyc"
            BAD_STARTERS = '#', '.'
            for ender in BAD_ENDERS:
                if file_name.endswith(ender):
                    return False
            for starter in BAD_STARTERS:
                if file_name.startswith(starter):
                    return False
            return True

        for (this_dir, dir_names, file_names) in os.walk(start_at):
            new_dir = DirNode(this_dir)
            self.dir_nodes += [new_dir]
            for file_name in sorted(file_names):
                if not IsGood(file_name):
                    continue
                new_dir.AddFileNode(FileNode(new_dir, file_name))

    def __str__(self):
        return_str = '\n'.join(str(n) for n in sorted(self.dir_nodes, key=lambda d:d.dir_name))
        return f"""
{return_str}
------
{len(self.dir_nodes):4} directories
{sum([len(d.file_nodes)for d in self.dir_nodes]):4} files
------
"""
            

def main():
    if len(sys.argv) == 2:
        dir_name = sys.argv[1]
    else:
        dir_name = input("dir name or nothing for current dir: ")
        
    if not dir_name:
        dir_name = '.'
        
    tree = Tree(dir_name)
    print(tree)
    

if __name__ == "__main__":
    main()

