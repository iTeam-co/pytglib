

from ..utils import Object


class ClosedVectorPath(Object):
    """
    Represents a closed vector path. The path begins at the end point of the last command 

    Attributes:
        ID (:obj:`str`): ``ClosedVectorPath``

    Args:
        commands (List of :class:`telegram.api.types.VectorPathCommand`):
            List of vector path commands

    Returns:
        ClosedVectorPath

    Raises:
        :class:`telegram.Error`
    """
    ID = "closedVectorPath"

    def __init__(self, commands, **kwargs):
        
        self.commands = commands  # list of VectorPathCommand

    @staticmethod
    def read(q: dict, *args) -> "ClosedVectorPath":
        commands = [Object.read(i) for i in q.get('commands', [])]
        return ClosedVectorPath(commands)
