

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
    def read(q: dict, *args) -> "PageBlockList or PageBlockVoiceNote or PageBlockTable or PageBlockSlideshow or PageBlockKicker or PageBlockRelatedArticles or PageBlockTitle or PageBlockDetails or PageBlockAuthorDate or PageBlockBlockQuote or PageBlockVideo or PageBlockAnimation or PageBlockDivider or PageBlockEmbeddedPost or PageBlockChatLink or PageBlockCover or PageBlockCollage or PageBlockMap or PageBlockFooter or PageBlockEmbedded or PageBlockParagraph or PageBlockPullQuote or PageBlockAnchor or PageBlockAudio or PageBlockPreformatted or PageBlockHeader or PageBlockPhoto or PageBlockSubheader or PageBlockSubtitle":
        if q.get("@type"):
            return Object.read(q)
        return PageBlock()
