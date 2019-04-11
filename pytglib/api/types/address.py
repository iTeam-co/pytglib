

from ..utils import Object


class Address(Object):
    """
    Describes an address 

    Attributes:
        ID (:obj:`str`): ``Address``

    Args:
        country_code (:obj:`str`):
            A two-letter ISO 3166-1 alpha-2 country code 
        state (:obj:`str`):
            State, if applicable 
        city (:obj:`str`):
            City 
        street_line1 (:obj:`str`):
            First line of the address 
        street_line2 (:obj:`str`):
            Second line of the address 
        postal_code (:obj:`str`):
            Address postal code

    Returns:
        Address

    Raises:
        :class:`telegram.Error`
    """
    ID = "address"

    def __init__(self, country_code, state, city, street_line1, street_line2, postal_code, **kwargs):
        
        self.country_code = country_code  # str
        self.state = state  # str
        self.city = city  # str
        self.street_line1 = street_line1  # str
        self.street_line2 = street_line2  # str
        self.postal_code = postal_code  # str

    @staticmethod
    def read(q: dict, *args) -> "Address":
        country_code = q.get('country_code')
        state = q.get('state')
        city = q.get('city')
        street_line1 = q.get('street_line1')
        street_line2 = q.get('street_line2')
        postal_code = q.get('postal_code')
        return Address(country_code, state, city, street_line1, street_line2, postal_code)
