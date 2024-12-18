import yaml
from pathlib import Path

class File:
    def __init__(self, path):
        self.path = path
        self.ext = path.split(".")[-1]
        self.content = self.load()

    def load(self):
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
        self.content = ""

    def load_html(self):
        self.content = ""

    def load_png(self):
        self.content = ""

    def __str__(self):
        return self.content