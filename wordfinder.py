import random
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """
    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> type(wf.random()) is str
    True
    """
    def __init__(self,path):
        self.path = path
        self.words = self.load_file()
        self.length = self.count()

    def load_file(self) -> list:
        file = open(self.path,'r')
        lines = file.readlines()
        return [line.strip() for line in lines]
        
    def random(self) -> str:
        return random.choice(self.words)
    
    def count(self) -> int:
        print(f'{len(self.words)} words read')
        return len(self.words)
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    """
    def __init__(self,path) -> None:
        super().__init__(path)
      
    def load_file(self):
        words = super().load_file()
        return [word.strip() for word in words if word.strip() and not word.startswith("#")]