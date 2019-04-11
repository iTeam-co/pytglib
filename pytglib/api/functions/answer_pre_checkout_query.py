

from ..utils import Object


class AnswerPreCheckoutQuery(Object):
    """
    Sets the result of a pre-checkout query; for bots only 

    Attributes:
        ID (:obj:`str`): ``AnswerPreCheckoutQuery``

    Args:
        pre_checkout_query_id (:obj:`int`):
            Identifier of the pre-checkout query 
        error_message (:obj:`str`):
            An error message, empty on success

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "answerPreCheckoutQuery"

    def __init__(self, pre_checkout_query_id, error_message, extra=None, **kwargs):
        self.extra = extra
        self.pre_checkout_query_id = pre_checkout_query_id  # int
        self.error_message = error_message  # str

    @staticmethod
    def read(q: dict, *args) -> "AnswerPreCheckoutQuery":
        pre_checkout_query_id = q.get('pre_checkout_query_id')
        error_message = q.get('error_message')
        return AnswerPreCheckoutQuery(pre_checkout_query_id, error_message)
