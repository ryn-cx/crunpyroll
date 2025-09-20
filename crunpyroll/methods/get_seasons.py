from crunpyroll import types
from crunpyroll.protocols import ClientProtocol
from typing import Any


class GetSeasons(ClientProtocol):
    async def download_seasons(
        self,
        series_id: str,
        *,
        preferred_audio_language: str | None = None,
        locale: str | None = None,
    ) -> dict[Any, Any]:
        """
        Download list of seasons from a series.

        Parameters:
            series_id (``str``):
                Unique identifier of the series.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.
            preferred_audio_language (``str``, *optional*):
                Audio language request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`dict`:
                Raw response data from the API.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/cms/series/" + series_id + "/seasons",
            params={
                "preferred_audio_language": preferred_audio_language
                or self.preferred_audio_language,
                "locale": locale or self.locale,
            },
        )

        if response is None:
            raise ValueError("Failed to download seasons.")

        return response

    async def get_seasons(
        self,
        series_id: str,
        *,
        preferred_audio_language: str | None = None,
        locale: str | None = None,
    ) -> types.SeasonsQuery:
        """
        Get list of seasons from a series.

        Parameters:
            series_id (``str``):
                Unique identifier of the series.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.
            preferred_audio_language (``str``, *optional*):
                Audio language request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`~crunpyroll.types.SeasonsQuery`:
                On success, query of seasons is returned.
        """
        response = await self.download_seasons(series_id, preferred_audio_language=preferred_audio_language, locale=locale)
        return types.SeasonsQuery.parse(response)
