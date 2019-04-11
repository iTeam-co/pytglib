

from ..utils import Object


class PageBlock(Object):
    """
    Describes a block of an instant view web page

    No parameters required.
    """
    ID = "pageBlock"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PageBlockAuthorDate or PageBlockDivider or PageBlockAnchor or PageBlockHeader or PageBlockFooter or PageBlockCollage or PageBlockAnimation or PageBlockVideo or PageBlockTitle or PageBlockPullQuote or PageBlockList or PageBlockPreformatted or PageBlockEmbedded or PageBlockEmbeddedPost or PageBlockChatLink or PageBlockParagraph or PageBlockCover or PageBlockPhoto or PageBlockAudio or PageBlockSlideshow or PageBlockSubtitle or PageBlockBlockQuote or PageBlockSubheader":
        if q.get("@type"):
            return Object.read(q)
        return PageBlock()
