from crunpyroll import types

import crunpyroll

class GetSeasons:
    async def download_seasons(
        self: "crunpyroll.Client",
        series_id: str,
        *,
        preferred_audio_language: str = None,
        locale: str = None,
    ) -> dict:
        """
        Download seasons data from a series.

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
            ``dict``:
                Raw API response data.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/cms/series/" + series_id + "/seasons",
            params={
                "preferred_audio_language": preferred_audio_language or self.preferred_audio_language,
                "locale": locale or self.locale
            }
        )
        return response

    def parse_seasons(
        self: "crunpyroll.Client",
        response: dict
    ) -> "types.SeasonsQuery":
        """
        Parse seasons data into SeasonsQuery object.

        Parameters:
            response (``dict``):
                Raw API response data.
                
        Returns:
            :obj:`~crunpyroll.types.SeasonsQuery`:
                Parsed seasons query object.
        """
        return types.SeasonsQuery.parse(response)

    async def get_seasons(
        self: "crunpyroll.Client",
        series_id: str,
        *,
        preferred_audio_language: str = None,
        locale: str = None,
    ) -> "types.SeasonsQuery":
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
        return self.parse_seasons(response)