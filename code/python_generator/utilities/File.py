import yaml
from pathlib import Path
from typing import List

class File:
    def __init__(self, path):
        self.path = path
        self.ext = path.split(".")[-1]
        self.load()

    def load(self):
        """
        content is a string that contains the content of the file
        """
        match self.ext:
            case "pdf":
                return self.load_pdf()
            case "txt":
                return self.load_txt()
            case "png":
                return self.load_png()
            case "html":
                return self.load_html()
            case _:
                self.content = ""
                print(f"Failed to load content, {self.ext} not recognized")
                return
    
    def load_pdf(self):
        self.content = ""

    def load_txt(self):
        with open(self.path, 'r') as f:
            self.content = str(f.read())

    def load_html(self):
        self.content = ""

    def load_png(self):
        self.content = ""

    def __str__(self):
        return self.content
    
    def __repr__(self):
        return str(self.path) + ": \n" + str(self.content) + "\n"
    

class MergedFiles:
    def __init__(self, files: List[File]):
        self.files = files
        self.content = ""
        self.merge()

    def merge(self):
        self.content = ""
        for file in self.files:
            self.content += f'Filename: "{file.path}"\n"""\n{file}\n"""\n\n'
    
    def __str__(self):
        return self.content
    
    def __repr__(self):
        return str(self.content)