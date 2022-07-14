

from ..utils import Object


class StatisticalValue(Object):
    """
    A value with information about its recent changes 

    Attributes:
        ID (:obj:`str`): ``StatisticalValue``

    Args:
        value (:obj:`float`):
            The current value 
        previous_value (:obj:`float`):
            The value for the previous day 
        growth_rate_percentage (:obj:`float`):
            The growth rate of the value, as a percentage

    Returns:
        StatisticalValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "statisticalValue"

    def __init__(self, value, previous_value, growth_rate_percentage, **kwargs):
        
        self.value = value  # float
        self.previous_value = previous_value  # float
        self.growth_rate_percentage = growth_rate_percentage  # float

    @staticmethod
    def read(q: dict, *args) -> "StatisticalValue":
        value = q.get('value')
        previous_value = q.get('previous_value')
        growth_rate_percentage = q.get('growth_rate_percentage')
        return StatisticalValue(value, previous_value, growth_rate_percentage)
