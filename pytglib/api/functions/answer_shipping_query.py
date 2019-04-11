

from ..utils import Object


class AnswerShippingQuery(Object):
    """
    Sets the result of a shipping query; for bots only 

    Attributes:
        ID (:obj:`str`): ``AnswerShippingQuery``

    Args:
        shipping_query_id (:obj:`int`):
            Identifier of the shipping query 
        shipping_options (List of :class:`telegram.api.types.shippingOption`):
            Available shipping options 
        error_message (:obj:`str`):
            An error message, empty on success

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "answerShippingQuery"

    def __init__(self, shipping_query_id, shipping_options, error_message, extra=None, **kwargs):
        self.extra = extra
        self.shipping_query_id = shipping_query_id  # int
        self.shipping_options = shipping_options  # list of shippingOption
        self.error_message = error_message  # str

    @staticmethod
    def read(q: dict, *args) -> "AnswerShippingQuery":
        shipping_query_id = q.get('shipping_query_id')
        shipping_options = [Object.read(i) for i in q.get('shipping_options', [])]
        error_message = q.get('error_message')
        return AnswerShippingQuery(shipping_query_id, shipping_options, error_message)
