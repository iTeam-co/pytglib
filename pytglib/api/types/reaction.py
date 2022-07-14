

from ..utils import Object


class Reaction(Object):
    """
    Contains stickers which must be used for reaction animation rendering

    Attributes:
        ID (:obj:`str`): ``Reaction``

    Args:
        reaction (:obj:`str`):
            Text representation of the reaction
        title (:obj:`str`):
            Reaction title
        is_active (:obj:`bool`):
            True, if the reaction can be added to new messages and enabled in chats
        is_premium (:obj:`bool`):
            True, if the reaction is available only for Premium users
        static_icon (:class:`telegram.api.types.sticker`):
            Static icon for the reaction
        appear_animation (:class:`telegram.api.types.sticker`):
            Appear animation for the reaction
        select_animation (:class:`telegram.api.types.sticker`):
            Select animation for the reaction
        activate_animation (:class:`telegram.api.types.sticker`):
            Activate animation for the reaction
        effect_animation (:class:`telegram.api.types.sticker`):
            Effect animation for the reaction
        around_animation (:class:`telegram.api.types.sticker`):
            Around animation for the reaction; may be null
        center_animation (:class:`telegram.api.types.sticker`):
            Center animation for the reaction; may be null

    Returns:
        Reaction

    Raises:
        :class:`telegram.Error`
    """
    ID = "reaction"

    def __init__(self, reaction, title, is_active, is_premium, static_icon, appear_animation, select_animation, activate_animation, effect_animation, around_animation, center_animation, **kwargs):
        
        self.reaction = reaction  # str
        self.title = title  # str
        self.is_active = is_active  # bool
        self.is_premium = is_premium  # bool
        self.static_icon = static_icon  # Sticker
        self.appear_animation = appear_animation  # Sticker
        self.select_animation = select_animation  # Sticker
        self.activate_animation = activate_animation  # Sticker
        self.effect_animation = effect_animation  # Sticker
        self.around_animation = around_animation  # Sticker
        self.center_animation = center_animation  # Sticker

    @staticmethod
    def read(q: dict, *args) -> "Reaction":
        reaction = q.get('reaction')
        title = q.get('title')
        is_active = q.get('is_active')
        is_premium = q.get('is_premium')
        static_icon = Object.read(q.get('static_icon'))
        appear_animation = Object.read(q.get('appear_animation'))
        select_animation = Object.read(q.get('select_animation'))
        activate_animation = Object.read(q.get('activate_animation'))
        effect_animation = Object.read(q.get('effect_animation'))
        around_animation = Object.read(q.get('around_animation'))
        center_animation = Object.read(q.get('center_animation'))
        return Reaction(reaction, title, is_active, is_premium, static_icon, appear_animation, select_animation, activate_animation, effect_animation, around_animation, center_animation)
