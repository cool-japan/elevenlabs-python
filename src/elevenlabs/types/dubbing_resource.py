# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .dubbing_media_reference import DubbingMediaReference
from .speaker_track import SpeakerTrack
from .speaker_segment import SpeakerSegment
from .render import Render
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class DubbingResource(UncheckedBaseModel):
    id: str
    version: int
    source_language: str
    target_languages: typing.List[str]
    input: DubbingMediaReference
    background: DubbingMediaReference
    foreground: DubbingMediaReference
    speaker_tracks: typing.Dict[str, SpeakerTrack]
    speaker_segments: typing.Dict[str, SpeakerSegment]
    renders: typing.Dict[str, Render]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
