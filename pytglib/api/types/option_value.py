

from ..utils import Object


class OptionValue(Object):
    """
    Represents the value of an option

    No parameters required.
    """
    ID = "optionValue"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "OptionValueEmpty or OptionValueString or OptionValueBoolean or OptionValueInteger":
        if q.get("@type"):
            return Object.read(q)
        return OptionValue()
