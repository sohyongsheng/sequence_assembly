class Error(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class InvalidNucleotide(Error):
    def __init__(self, message):
        super().__init__(message)

