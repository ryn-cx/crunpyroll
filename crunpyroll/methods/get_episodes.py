from crunpyroll import types
from crunpyroll.protocols import ClientProtocol
from typing import Any


class GetEpisodes(ClientProtocol):
    async def download_episodes(
        self,
        season_id: str,
        *,
        locale: str | None = None,
    ) -> dict[Any, Any]:
        """
        Download list of episodes from a season.

        Parameters:
            season_id (``str``):
                Unique identifier of the season.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`dict`:
                Raw response data from the API.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/cms/seasons/" + season_id + "/episodes",
            params={"locale": locale or self.locale},
        )

        if response is None:
            raise ValueError("Failed to download episodes.")

        return response

    async def get_episodes(
        self,
        season_id: str,
        *,
        locale: str | None = None,
    ) -> types.EpisodesQuery:
        """
        Get list of episodes from a season.

        Parameters:
            season_id (``str``):
                Unique identifier of the season.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`~crunpyroll.types.EpisodesQuery`:
                On success, query of episodes is returned.
        """
        response = await self.download_episodes(season_id, locale=locale)
        return types.EpisodesQuery.parse(response)
