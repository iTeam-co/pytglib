

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
    def read(q: dict, *args) -> "PageBlockSubtitle or PageBlockPhoto or PageBlockDivider or PageBlockRelatedArticles or PageBlockSubheader or PageBlockVideo or PageBlockFooter or PageBlockTitle or PageBlockParagraph or PageBlockCollage or PageBlockAnimation or PageBlockSlideshow or PageBlockPullQuote or PageBlockList or PageBlockAuthorDate or PageBlockAnchor or PageBlockDetails or PageBlockHeader or PageBlockAudio or PageBlockPreformatted or PageBlockChatLink or PageBlockBlockQuote or PageBlockKicker or PageBlockEmbeddedPost or PageBlockCover or PageBlockEmbedded or PageBlockVoiceNote or PageBlockTable or PageBlockMap":
        if q.get("@type"):
            return Object.read(q)
        return PageBlock()
