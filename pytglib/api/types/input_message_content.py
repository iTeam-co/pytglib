

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
    def read(q: dict, *args) -> "InputMessageGame or InputMessageAnimation or InputMessageText or InputMessageVoiceNote or InputMessageLocation or InputMessageForwarded or InputMessageVenue or InputMessageVideoNote or InputMessageVideo or InputMessageDocument or InputMessageContact or InputMessageSticker or InputMessageInvoice or InputMessageAudio or InputMessagePhoto":
        if q.get("@type"):
            return Object.read(q)
        return InputMessageContent()
