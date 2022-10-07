"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,*,start):
        self.start = start
        self.inc = start
        
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.inc}>"

    def generate(self):
        og = self.inc
        self.inc += 1
        return og
    
    def reset(self):
        self.inc = self.start    
        
