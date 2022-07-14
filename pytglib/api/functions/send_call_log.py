

from ..utils import Object


class SendCallLog(Object):
    """
    Sends log file for a call to Telegram servers 

    Attributes:
        ID (:obj:`str`): ``SendCallLog``

    Args:
        call_id (:obj:`int`):
            Call identifier 
        log_file (:class:`telegram.api.types.InputFile`):
            Call log fileOnly inputFileLocal and inputFileGenerated are supported

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendCallLog"

    def __init__(self, call_id, log_file, extra=None, **kwargs):
        self.extra = extra
        self.call_id = call_id  # int
        self.log_file = log_file  # InputFile

    @staticmethod
    def read(q: dict, *args) -> "SendCallLog":
        call_id = q.get('call_id')
        log_file = Object.read(q.get('log_file'))
        return SendCallLog(call_id, log_file)
