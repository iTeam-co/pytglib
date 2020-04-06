

from ..utils import Object


class WebPage(Object):
    """
    Describes a web page preview

    Attributes:
        ID (:obj:`str`): ``WebPage``

    Args:
        url (:obj:`str`):
            Original URL of the link
        display_url (:obj:`str`):
            URL to display
        type (:obj:`str`):
            Type of the web pageCan be: article, photo, audio, video, document, profile, app, or something else
        site_name (:obj:`str`):
            Short name of the site (eg, Google Docs, App Store)
        title (:obj:`str`):
            Title of the content
        description (:class:`telegram.api.types.formattedText`):
            Description of the content
        photo (:class:`telegram.api.types.photo`):
            Image representing the content; may be null
        embed_url (:obj:`str`):
            URL to show in the embedded preview
        embed_type (:obj:`str`):
            MIME type of the embedded preview, (eg, text/html or video/mp4)
        embed_width (:obj:`int`):
            Width of the embedded preview
        embed_height (:obj:`int`):
            Height of the embedded preview
        duration (:obj:`int`):
            Duration of the content, in seconds
        author (:obj:`str`):
            Author of the content
        animation (:class:`telegram.api.types.animation`):
            Preview of the content as an animation, if available; may be null
        audio (:class:`telegram.api.types.audio`):
            Preview of the content as an audio file, if available; may be null
        document (:class:`telegram.api.types.document`):
            Preview of the content as a document, if available (currently only available for small PDF files and ZIP archives); may be null
        sticker (:class:`telegram.api.types.sticker`):
            Preview of the content as a sticker for small WEBP files, if available; may be null
        video (:class:`telegram.api.types.video`):
            Preview of the content as a video, if available; may be null
        video_note (:class:`telegram.api.types.videoNote`):
            Preview of the content as a video note, if available; may be null
        voice_note (:class:`telegram.api.types.voiceNote`):
            Preview of the content as a voice note, if available; may be null
        instant_view_version (:obj:`int`):
            Version of instant view, available for the web page (currently can be 1 or 2), 0 if none

    Returns:
        WebPage

    Raises:
        :class:`telegram.Error`
    """
    ID = "webPage"

    def __init__(self, url, display_url, type, site_name, title, description, photo, embed_url, embed_type, embed_width, embed_height, duration, author, animation, audio, document, sticker, video, video_note, voice_note, instant_view_version, **kwargs):
        
        self.url = url  # str
        self.display_url = display_url  # str
        self.type = type  # str
        self.site_name = site_name  # str
        self.title = title  # str
        self.description = description  # FormattedText
        self.photo = photo  # Photo
        self.embed_url = embed_url  # str
        self.embed_type = embed_type  # str
        self.embed_width = embed_width  # int
        self.embed_height = embed_height  # int
        self.duration = duration  # int
        self.author = author  # str
        self.animation = animation  # Animation
        self.audio = audio  # Audio
        self.document = document  # Document
        self.sticker = sticker  # Sticker
        self.video = video  # Video
        self.video_note = video_note  # VideoNote
        self.voice_note = voice_note  # VoiceNote
        self.instant_view_version = instant_view_version  # int

    @staticmethod
    def read(q: dict, *args) -> "WebPage":
        url = q.get('url')
        display_url = q.get('display_url')
        type = q.get('type')
        site_name = q.get('site_name')
        title = q.get('title')
        description = Object.read(q.get('description'))
        photo = Object.read(q.get('photo'))
        embed_url = q.get('embed_url')
        embed_type = q.get('embed_type')
        embed_width = q.get('embed_width')
        embed_height = q.get('embed_height')
        duration = q.get('duration')
        author = q.get('author')
        animation = Object.read(q.get('animation'))
        audio = Object.read(q.get('audio'))
        document = Object.read(q.get('document'))
        sticker = Object.read(q.get('sticker'))
        video = Object.read(q.get('video'))
        video_note = Object.read(q.get('video_note'))
        voice_note = Object.read(q.get('voice_note'))
        instant_view_version = q.get('instant_view_version')
        return WebPage(url, display_url, type, site_name, title, description, photo, embed_url, embed_type, embed_width, embed_height, duration, author, animation, audio, document, sticker, video, video_note, voice_note, instant_view_version)
