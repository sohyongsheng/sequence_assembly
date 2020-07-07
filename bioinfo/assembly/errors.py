from bioinfo.error import Error

class InvalidPair(Error):
    def __init__(self, message):
        super().__init__(message)

