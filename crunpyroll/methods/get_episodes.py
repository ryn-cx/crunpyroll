from crunpyroll import types
from typing import Any

import crunpyroll


class GetEpisodes:
    async def download_episodes(
        self: "crunpyroll.Client", season_id: str, *, locale: str = None
    ) -> dict[str, Any]:
        """
        Download episodes data from a season.

        Parameters:
            season_id (``str``):
                Unique identifier of the season.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            ``dict``:
                Raw API response data.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/cms/seasons/" + season_id + "/episodes",
            params={"locale": locale or self.locale},
        )
        return response

    def parse_episodes(
        self: "crunpyroll.Client", response: dict
    ) -> "types.EpisodesQuery":
        """
        Parse episodes data into EpisodesQuery object.

        Parameters:
            response (``dict``):
                Raw API response data.

        Returns:
            :obj:`~crunpyroll.types.EpisodesQuery`:
                Parsed episodes query object.
        """
        return types.EpisodesQuery.parse(response)

    async def get_episodes(
        self: "crunpyroll.Client", season_id: str, *, locale: str = None
    ) -> "types.EpisodesQuery":
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
        return self.parse_episodes(response)
