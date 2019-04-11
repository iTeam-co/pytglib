

from ..utils import Object


class TestSquareInt(Object):
    """
    Returns the squared received number; for testing only 

    Attributes:
        ID (:obj:`str`): ``TestSquareInt``

    Args:
        x (:obj:`int`):
            Number to square

    Returns:
        TestInt

    Raises:
        :class:`telegram.Error`
    """
    ID = "testSquareInt"

    def __init__(self, x, extra=None, **kwargs):
        self.extra = extra
        self.x = x  # int

    @staticmethod
    def read(q: dict, *args) -> "TestSquareInt":
        x = q.get('x')
        return TestSquareInt(x)
