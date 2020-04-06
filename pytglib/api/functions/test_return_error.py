

from ..utils import Object


class TestReturnError(Object):
    """
    Returns the specified error and ensures that the Error object is used; for testing only. This is an offline method. Can be called before authorization. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``TestReturnError``

    Args:
        error (:class:`telegram.api.types.error`):
            The error to be returned

    Returns:
        Error

    Raises:
        :class:`telegram.Error`
    """
    ID = "testReturnError"

    def __init__(self, error, extra=None, **kwargs):
        self.extra = extra
        self.error = error  # Error

    @staticmethod
    def read(q: dict, *args) -> "TestReturnError":
        error = Object.read(q.get('error'))
        return TestReturnError(error)
