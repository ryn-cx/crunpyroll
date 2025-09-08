from crunpyroll import types
from typing import Any

import crunpyroll


class GetSeries:
    async def download_series(
        self: "crunpyroll.Client",
        series_id: str,
        *,
        locale: str = None,
    ) -> dict[str, Any]:
        """
        Download series data.

        Parameters:
            series_id (``str``):
                Unique identifier of the series.
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
            endpoint="content/v2/cms/series/" + series_id,
            params={"locale": locale or self.locale},
        )
        return response

    def parse_series(self: "crunpyroll.Client", response: dict) -> "types.Series":
        """
        Parse series data into Series object.

        Parameters:
            response (``dict``):
                Raw API response data.

        Returns:
            :obj:`~crunpyroll.types.Series`:
                Parsed series object.
        """
        return types.Series.parse(response)

    async def get_series(
        self: "crunpyroll.Client",
        series_id: str,
        *,
        locale: str = None,
    ) -> "types.Series":
        """
        Get informations about a series.

        Parameters:
            series_id (``str``):
                Unique identifier of the series.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`~crunpyroll.types.Series`:
                On success, series object is returned.
        """
        response = await self.download_series(series_id, locale=locale)
        return self.parse_series(response)
