

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
    def read(q: dict, *args) -> "PageBlockAnchor or PageBlockMap or PageBlockEmbedded or PageBlockPreformatted or PageBlockTable or PageBlockVideo or PageBlockSubheader or PageBlockDivider or PageBlockSlideshow or PageBlockEmbeddedPost or PageBlockKicker or PageBlockPullQuote or PageBlockCover or PageBlockBlockQuote or PageBlockDetails or PageBlockAuthorDate or PageBlockPhoto or PageBlockSubtitle or PageBlockTitle or PageBlockCollage or PageBlockFooter or PageBlockAudio or PageBlockRelatedArticles or PageBlockHeader or PageBlockChatLink or PageBlockAnimation or PageBlockParagraph or PageBlockList":
        if q.get("@type"):
            return Object.read(q)
        return PageBlock()
