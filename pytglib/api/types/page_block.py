

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
    def read(q: dict, *args) -> "PageBlockTable or PageBlockCollage or PageBlockFooter or PageBlockKicker or PageBlockPullQuote or PageBlockChatLink or PageBlockPreformatted or PageBlockCover or PageBlockSubtitle or PageBlockSubheader or PageBlockMap or PageBlockEmbedded or PageBlockSlideshow or PageBlockTitle or PageBlockHeader or PageBlockPhoto or PageBlockAudio or PageBlockEmbeddedPost or PageBlockAuthorDate or PageBlockBlockQuote or PageBlockVideo or PageBlockAnimation or PageBlockRelatedArticles or PageBlockAnchor or PageBlockDetails or PageBlockParagraph or PageBlockDivider or PageBlockList":
        if q.get("@type"):
            return Object.read(q)
        return PageBlock()
