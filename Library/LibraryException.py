
class BookException(Exception):
    _code = 0
    _msg = ''

    def __init__(self, code: int = 0, msg: str = ''):
        self._code = code
        self._msg = msg

    def GetErrorCode(self)-> int:
        return self._code

    def GetErrorMessage(self)-> str:
        return self._msg