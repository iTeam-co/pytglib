

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
    def read(q: dict, *args) -> "InputMessageDice or InputMessageSticker or InputMessageVenue or InputMessageGame or InputMessageText or InputMessagePoll or InputMessageForwarded or InputMessagePhoto or InputMessageInvoice or InputMessageLocation or InputMessageVideoNote or InputMessageDocument or InputMessageVideo or InputMessageVoiceNote or InputMessageContact or InputMessageAudio or InputMessageAnimation":
        if q.get("@type"):
            return Object.read(q)
        return InputMessageContent()
