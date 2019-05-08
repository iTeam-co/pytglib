

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
    def read(q: dict, *args) -> "InputMessageVideo or InputMessageDocument or InputMessageLocation or InputMessagePoll or InputMessageAnimation or InputMessageGame or InputMessagePhoto or InputMessageContact or InputMessageVideoNote or InputMessageForwarded or InputMessageInvoice or InputMessageVenue or InputMessageAudio or InputMessageSticker or InputMessageVoiceNote or InputMessageText":
        if q.get("@type"):
            return Object.read(q)
        return InputMessageContent()
