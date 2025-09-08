from crunpyroll import types
from typing import Any

import crunpyroll


class GetObjects:
    async def download_objects(
        self: "crunpyroll.Client",
        object_id: str,
        *,
        preferred_audio_language: str = None,
        locale: str = None,
    ) -> dict[str, Any]:
        """
        Download object data from an id.

        Parameters:
            object_id (``str``):
                Unique identifier of the episode.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.
            preferred_audio_language (``str``, *optional*):
                Audio language request for different results.
                Default to the one used in Client.

        Returns:
            ``dict``:
                Raw API response data.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/cms/objects/" + object_id,
            params={
                "preferred_audio_language": preferred_audio_language
                or self.preferred_audio_language,
                "locale": locale or self.locale,
            },
        )
        return response

    def parse_objects(
        self: "crunpyroll.Client", response: dict
    ) -> "types.ObjectsQuery":
        """
        Parse object data into ObjectsQuery.

        Parameters:
            response (``dict``):
                Raw API response data.

        Returns:
            :obj:`~crunpyroll.types.ObjectsQuery`:
                Parsed objects query.
        """
        return types.ObjectsQuery.parse(response)

    async def get_objects(
        self: "crunpyroll.Client",
        object_id: str,
        *,
        preferred_audio_language: str = None,
        locale: str = None,
    ) -> "types.ObjectsQuery":
        """
        Get series/season/episode/movie from an id. This method may miss some data.
        Missing attributes:
            Season: ``episode_count``, ``is_simulcast``, ``is_subbed``, ``is_dubbed``.
            Episode: ``next_episode_title``, ``next_episode_id``, ``is_hd``.
            Movie: ``is_new``.
        Parameters:
            object_id (``str``):
                Unique identifier of the episode.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            (:obj:`~crunpyroll.types.Series` | :obj:`~crunpyroll.types.Season` | :obj:`~crunpyroll.types.Episode` | :obj:`~crunpyroll.types.Movie`):
                On success, series/season/episode/movie object is returned.
        """
        response = await self.download_objects(
            object_id, preferred_audio_language=preferred_audio_language, locale=locale
        )
        return self.parse_objects(response)
