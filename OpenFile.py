'''
Carlo Baltao

ADEV-3005 (254275)

Topic Challenge - Module 4F

2024-09-27
'''

class OpenFile:
    def __init__(self, filename, mode):
        """Initializes the OpenFile class with the filename and its open mode as parameters."""
        self.filename = filename
        self.mode = mode
        self.file_handle = None

    def __enter__(self):
        """Opens and returns the file handle of the file when executed in the 'with' block."""
        self.file_handle = open(self.filename, self.mode)
        return self.file_handle

    def __exit__(self, exc_type, exc_value, traceback):
        """Upon the exiting the 'with' block, the file will be closed if the file handle exists."""
        if self.file_handle:
            self.file_handle.close()

with OpenFile('TestFile.txt', 'r') as file:
    content = file.read()
    print(content)
