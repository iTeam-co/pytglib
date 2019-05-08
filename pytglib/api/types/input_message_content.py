

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
    def read(q: dict, *args) -> "InputMessageDocument or InputMessageVideoNote or InputMessageLocation or InputMessageInvoice or InputMessageVideo or InputMessageContact or InputMessagePoll or InputMessageAnimation or InputMessageGame or InputMessageText or InputMessageForwarded or InputMessageVoiceNote or InputMessageSticker or InputMessageVenue or InputMessageAudio or InputMessagePhoto":
        if q.get("@type"):
            return Object.read(q)
        return InputMessageContent()
