

from ..utils import Object


class PollOption(Object):
    """
    Describes one answer option of a poll 

    Attributes:
        ID (:obj:`str`): ``PollOption``

    Args:
        text (:obj:`str`):
            Option text, 1-100 characters 
        voter_count (:obj:`int`):
            Number of voters for this option, available only for closed or voted polls 
        vote_percentage (:obj:`int`):
            The percentage of votes for this option, 0-100
        is_chosen (:obj:`bool`):
            True, if the option was chosen by the user 
        is_being_chosen (:obj:`bool`):
            True, if the option is being chosen by a pending setPollAnswer request

    Returns:
        PollOption

    Raises:
        :class:`telegram.Error`
    """
    ID = "pollOption"

    def __init__(self, text, voter_count, vote_percentage, is_chosen, is_being_chosen, **kwargs):
        
        self.text = text  # str
        self.voter_count = voter_count  # int
        self.vote_percentage = vote_percentage  # int
        self.is_chosen = is_chosen  # bool
        self.is_being_chosen = is_being_chosen  # bool

    @staticmethod
    def read(q: dict, *args) -> "PollOption":
        text = q.get('text')
        voter_count = q.get('voter_count')
        vote_percentage = q.get('vote_percentage')
        is_chosen = q.get('is_chosen')
        is_being_chosen = q.get('is_being_chosen')
        return PollOption(text, voter_count, vote_percentage, is_chosen, is_being_chosen)
