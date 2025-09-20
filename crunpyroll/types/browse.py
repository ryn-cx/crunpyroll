from ..enums import ContentType
from ..utils import str_to_date

from .obj import Object
from .series import Series
from .episodes import Episode
from .movies import Movie

from typing import Any
from datetime import datetime


class BrowseSeries(Series):
    """
    Series info from browse endpoint that includes last_public date.

    Parameters:
        id (``str``):
            Unique identifier of the series.

        title (``str``):
            Title of the series.

        slug (``str``):
            Slug of the series.

        description (``str``):
            Number of the series.

        season_count (``int``):
            Season count of the series.

        episode_count (``int``):
            Episode count of the series.

        launch_year (``int``):
            Leanch year of the series.

        subtitle_locales (List of ``str``):
            List containing language codes of available subtitles.

        audio_locales (``str``):
            Language code of the audio.

        maturity_ratings (List of ``str``)

        is_simulcast (``bool``):
            True, if this season is simulcast (currently airing).

        is_subbed (``bool``):
            True, if this season got subtitles.

        is_dubbed (``bool``):
            True, if this season got dubs.

        is_mature (``bool``):
            True, if this season is NSFW.
        last_public (:py:obj:`~datetime.datetime`):
            Date when the series was last made public.
    """

    def __init__(self, data: dict[Any, Any]):
        super().__init__(data)
        self.last_updated = str_to_date(data.get("last_public"))


class BrowseEpisode(Episode):
    """
    Episode info from browse endpoint that includes last_public date.

    Parameters:
        id (``str``):
            Unique identifier of the series.

        title (``str``):
            Title of the series.

        slug (``str``):
            Slug of the series.

        description (``str``):
            Number of the series.

        season_count (``int``):
            Season count of the series.

        episode_count (``int``):
            Episode count of the series.

        launch_year (``int``):
            Leanch year of the series.

        subtitle_locales (List of ``str``):
            List containing language codes of available subtitles.

        audio_locales (``str``):
            Language code of the audio.

        maturity_ratings (List of ``str``)

        is_simulcast (``bool``):
            True, if this season is simulcast (currently airing).

        is_subbed (``bool``):
            True, if this season got subtitles.

        is_dubbed (``bool``):
            True, if this season got dubs.

        is_mature (``bool``):
            True, if this season is NSFW.

        last_public (:py:obj:`~datetime.datetime`):
            Date when the episode was last made public.
    """

    def __init__(self, data: dict[Any, Any]):
        super().__init__(data)
        self.last_updated = str_to_date(data.get("last_public"))


class BrowseMovie(Movie):
    """
    Movie info from browse endpoint that includes last_public date.
    Parameters:
        id (``str``):
            Unique identifier of the movie.

        title (``str``):
            Title of the movie.

        slug (``str``):
            Slug of the movie.

        duration (``int``):
            Duration of the movie.

        free_available_date (:py:obj:`~datetime.datetime`):
            Date the movie will be released to free users.

        premium_available_date (:py:obj:`~datetime.datetime`):
            Date the movie will be released to premium users.

        release_year (``int``):
            Year the movie was released.

        description (``str``):
            Description of the movie.

        first_movie_id (``str``)

        subtitle_locales (List of ``str``):
            List containing language codes of available subtitles.

        audio_locales (``str``):
            Language code of the audio.

        maturity_ratings (List of ``str``)

        images (:obj:`~crunpyroll.types.Images`):
            Images of the movie.

        has_closed_captions (``bool``):
            True, if this movie got closed captions.

        is_available_offline (``bool``):
            True, if this movie is available offline.

        is_hd (``bool``):
            True, if this movie is High Definition.

        is_new (``bool``):
            True, if this movie is newly released.

        is_premium (``bool``):
            True, if this movie is available to premium users only.

        is_simulcast (``bool``):
            True, if this movie is simulcast (currently airing).

        is_subbed (``bool``):
            True, if this movie got subtitles.

        is_dubbed (``bool``):
            True, if this movie got dubs.

        is_mature (``bool``):
            True, if this movie is NSFW.

        last_public (:py:obj:`~datetime.datetime`):
            Date when the movie was last modified.
    """

    def __init__(self, data: dict[Any, Any]):
        super().__init__(data)
        self.last_updated = str_to_date(data.get("last_public"))


ITEMS_TYPING = list[BrowseSeries | BrowseEpisode | BrowseMovie]


class BrowseQuery(Object):
    """
    Query containing browse results.

    Parameters:
        total (``int``):
            Total results returned.

        items (List of [:obj:`~crunpyroll.types.Series` | :obj:`~crunpyroll.types.Episode` | :obj:`~crunpyroll.types.Movie`]):
            List containing each result.
    """

    def __init__(self, total: int, items: ITEMS_TYPING):
        self.total = total
        self.items = items

    @classmethod
    def parse(cls, response: dict[Any, Any]):
        items: ITEMS_TYPING = []
        for item in response["data"]:
            if item["type"] == ContentType.SERIES.value:
                items.append(BrowseSeries.parse(item))
            elif item["type"] == ContentType.EPISODE.value:
                items.append(BrowseEpisode.parse(item))
            elif item["type"] == ContentType.MOVIE.value:
                items.append(BrowseMovie.parse(item))
        return cls(len(items), items)
