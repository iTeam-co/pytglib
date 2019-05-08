

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
    def read(q: dict, *args) -> "OptionValueInteger or OptionValueBoolean or OptionValueString or OptionValueEmpty":
        if q.get("@type"):
            return Object.read(q)
        return OptionValue()
