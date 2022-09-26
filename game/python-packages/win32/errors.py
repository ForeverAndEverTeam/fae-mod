class FAEWin32Error(Exception):
    """
    Base class for exceptions
    """

class Win32Error(FAEWin32Error):
    def __init__(self, msg: str, code: int):
        self.msg = msg
        self.code = code
    
    def __str__(self) -> str:
        return f"{self.msg}. Status code: {self.code}"

class NotifError(FAEWin32Error):
    """
    Base class for notifs
    """

class ManagerAlreadyExistsError(NotifError):

    def __str__(self) -> str:
        return "notification manager has already been defined."