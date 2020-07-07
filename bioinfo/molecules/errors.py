from bioinfo.error import Error

class InvalidNucleotide(Error):
    def __init__(self, message):
        super().__init__(message)

