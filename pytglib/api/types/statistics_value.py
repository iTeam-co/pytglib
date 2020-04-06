

from ..utils import Object


class StatisticsValue(Object):
    """
    A statistics value 

    Attributes:
        ID (:obj:`str`): ``StatisticsValue``

    Args:
        value (:obj:`float`):
            The value 
        previous_value (:obj:`float`):
            The value for the previous day 
        growth_rate_percentage (:obj:`float`):
            The growth rate of the value, as a percentage

    Returns:
        StatisticsValue

    Raises:
        :class:`telegram.Error`
    """
    ID = "statisticsValue"

    def __init__(self, value, previous_value, growth_rate_percentage, **kwargs):
        
        self.value = value  # float
        self.previous_value = previous_value  # float
        self.growth_rate_percentage = growth_rate_percentage  # float

    @staticmethod
    def read(q: dict, *args) -> "StatisticsValue":
        value = q.get('value')
        previous_value = q.get('previous_value')
        growth_rate_percentage = q.get('growth_rate_percentage')
        return StatisticsValue(value, previous_value, growth_rate_percentage)
