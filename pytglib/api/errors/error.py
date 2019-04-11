class Error(Exception):
    """This is the base exception class for all TDLib API related errors."""
    CODE = None
    MESSAGE = None

    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.CODE = code
        self.MESSAGE = message
