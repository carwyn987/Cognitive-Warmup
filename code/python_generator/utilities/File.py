import yaml
from pathlib import Path
from typing import List
import numpy as np
import tiktoken

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

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

    def merge(self, prob=0.6):
        self.content = ""
        num_choose = int(len(self.files) * prob)
        selected_files = np.random.choice(self.files, num_choose, replace=False)
        for file in selected_files:
            self.content += f'Filename: "{file.path}"\n"""\n{file}\n"""\n\n'

    def get_content(self, random=True, tokens=120000):
        if not random:
            return NotImplementedError()
        if num_tokens_from_string(self.content) < tokens:
            return self.content
        _content = ""
        split_content = self.content.split("\n")
        while num_tokens_from_string(_content) < tokens:
            start_line = np.random.randint(0, len(split_content))
            end_line = start_line + (np.random.randint(6, 15) if start_line + 15 < len(split_content) else len(split_content) - start_line)
            _content += ''.join(split_content[start_line:end_line])

        while num_tokens_from_string(_content) > tokens:
            _content = _content[:-5]

        return _content
        
    
    def __str__(self):
        return self.content
    
    def __repr__(self):
        return str(self.content)