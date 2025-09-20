from crunpyroll import types
from crunpyroll.protocols import ClientProtocol
from typing import Any


class GetSeries(ClientProtocol):
    async def download_series(
        self,
        series_id: str,
        *,
        locale: str | None = None,
    ) -> dict[Any, Any]:
        """
        Download informations about a series.

        Parameters:
            series_id (``str``):
                Unique identifier of the series.
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
            endpoint="content/v2/cms/series/" + series_id,
            params={"locale": locale or self.locale},
        )

        if response is None:
            raise ValueError("Failed to download series.")

        return response

    async def get_series(
        self,
        series_id: str,
        *,
        locale: str | None = None,
    ) -> types.Series:
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
        return types.Series.parse(response)
