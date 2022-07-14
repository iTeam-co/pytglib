

from ..utils import Object


class Countries(Object):
    """
    Contains information about countries 

    Attributes:
        ID (:obj:`str`): ``Countries``

    Args:
        countries (List of :class:`telegram.api.types.countryInfo`):
            The list of countries

    Returns:
        Countries

    Raises:
        :class:`telegram.Error`
    """
    ID = "countries"

    def __init__(self, countries, **kwargs):
        
        self.countries = countries  # list of countryInfo

    @staticmethod
    def read(q: dict, *args) -> "Countries":
        countries = [Object.read(i) for i in q.get('countries', [])]
        return Countries(countries)
