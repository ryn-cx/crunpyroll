from crunpyroll import enums
from crunpyroll import types
from crunpyroll.utils import get_date
from crunpyroll.protocols import ClientProtocol
from datetime import datetime
from typing import Any


class Browse(ClientProtocol):
    async def download_browse(
        self,
        max_results: int,
        locale: str,
        filters_string: str,
        sort_by: str,
    ) -> dict[Any, Any]:
        """
        Download the browse response from the API.

        Parameters:
            max_results: Maximum number of results to return
            locale: Locale for the request
            filters_string: Comma-separated content type filters
            sort_by: Sort type value

        Returns:
            dict: Raw API response
        """
        response =  await self.api_request(
            method="GET",
            endpoint="content/v2/discover/browse",
            params={
                "n": max_results,
                "locale": locale,
                "type": filters_string,
                "sort_by": sort_by,
            },
        )

        if response is None:
            raise ValueError("Failed to download browse results.")
        
        return response

    # https://www.crunchyroll.com/content/v2/discover/browse?type=episode&sort_by=newly_added&n=100&preferred_audio_language=ja-JP&locale=en-US
    async def browse(
        self,
        sort_by: str = "newly_added",
        date: datetime = get_date(),
        max_results: int = 100,
        locale: str | None = None,
        filters: list["enums.ContentType"] = [
            enums.ContentType.SERIES,
            enums.ContentType.MOVIE,
            enums.ContentType.EPISODE,
            enums.ContentType.MUSIC,
        ],
    ) -> types.BrowseQuery:
        
        """
        Browse for series movies or episodes.

        Parameters:
            date: (``datetime``, *optional*):
                Get only contents release at this date
                Default date: current
            sort_by: (Value of :obj:`~crunpyroll.enums.SortType`, *optional*):
                Sort content
                Default to newly added :obj:`~crunpyroll.enums.NEWLY_ADDED`.
            max_results (``int``, *optional*):
                Max results for every content type.
                Default to 15
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.
            filters (List of :obj:`~crunpyroll.enums.ContentType`, *optional*):
                Content to filters.
                Default to every value in :obj:`~crunpyroll.enums.ContentType`.

        Returns:
            :obj:`~crunpyroll.types.BrowseQuery`:
                On success, query of results is returned.
        """
        await self.session.retrieve()

        filters_string = ",".join(
            filter.value for filter in filters if isinstance(filter, enums.ContentType)
        )

        response = await self.download_browse(
            max_results=max_results,
            locale=locale or self.locale,
            filters_string=filters_string,
            sort_by=sort_by,
        )

        return types.BrowseQuery.parse(date, response)
