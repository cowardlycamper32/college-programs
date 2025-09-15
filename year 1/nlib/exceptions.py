class NotANumberError(Exception):
    "Raised when presented value is not a number"
    pass

class LogNotOpenError(Exception):
    "Raised when opening a log that doesnt exist"
    pass

class LogFolderAlreadyExistsException(Exception):
    "Raised when a folder already exists"
    pass