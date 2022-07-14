

from ..utils import Object


class InputMessageContent(Object):
    """
    The content of a message to send

    No parameters required.
    """
    ID = "inputMessageContent"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "InputMessageDocument or InputMessageInvoice or InputMessageAnimation or InputMessageVoiceNote or InputMessageContact or InputMessageGame or InputMessageText or InputMessageSticker or InputMessageAudio or InputMessagePhoto or InputMessageLocation or InputMessageDice or InputMessageVideoNote or InputMessageVideo or InputMessageForwarded or InputMessagePoll or InputMessageVenue":
        if q.get("@type"):
            return Object.read(q)
        return InputMessageContent()
