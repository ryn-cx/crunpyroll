from crunpyroll import enums
from crunpyroll import types
from crunpyroll.utils import get_date
from crunpyroll.protocols import ClientProtocol
from datetime import datetime
from typing import Any


# Default values are based on the URL
# https://www.crunchyroll.com/content/v2/discover/browse?n=36&sort_by=newly_added&ratings=true&locale=en-US
# Which was found by scrolling down a little bit on https://www.crunchyroll.com/videos/new
# which is the home page.
# Fiters and preferred_audio_language are supported because URLs such as
# https://www.crunchyroll.com/content/v2/discover/browse?type=episode&sort_by=newly_added&n=100&preferred_audio_language=ja-JP&locale=en-US
# can be found on the home page https://www.crunchyroll.com/discover
class Browse(ClientProtocol):
    async def download_browse(
        self,
        sort_by: str = "newly_added",
        max_results: int = 36,
        start: int | None = None,
        filters: list[enums.ContentType] | None = None,
        preferred_audio_language: str | None = None,
        ratings: bool | None = True,
        locale: str | None = None,
    ) -> dict[Any, Any]:
        """
        Download browse results for series, movies or episodes.

        Parameters:
            sort_by (``str``, *optional*):
                Sort content by criteria.
                Default to "newly_added".
            max_results (``int``, *optional*):
                Max results for every content type.
                Default to 36.
            start (``int``, *optional*):
                Starting index for pagination.
                Default to None.
            filters (List of :obj:`~crunpyroll.enums.ContentType`, *optional*):
                Content types to filter by.
                Default to None (no filtering).
            preferred_audio_language (``str``, *optional*):
                Audio language request for different results.
                Default to the one used in Client.
            ratings (``bool``, *optional*):
                Include ratings in the response.
                Default to True.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`dict`:
                Raw response data from the API.
        """
        # Building the parameters like this means the parameters sent should exactly match
        # the ones sent by Crunchyroll's own website.
        params: dict[str, str | int] = {
            "n": max_results,
            "sort_by": sort_by,
            "locale": locale or self.locale,
        }
        if start is not None:
            params["start"] = start
        if ratings is not None:
            params["ratings"] = str(ratings).lower()
        if locale is not None:
            params["locale"] = locale
        if preferred_audio_language is not None:
            params["preferred_audio_language"] = preferred_audio_language
        if filters:
            params["type"] = ",".join(filter.value for filter in filters)

        response = await self.api_request(
            method="GET",
            endpoint="content/v2/discover/browse",
            params=params,
        )

        if response is None:
            raise ValueError("Failed to download browse results.")

        return response

    async def browse(
        self,
        sort_by: str = "newly_added",
        max_results: int = 36,
        filters: list["enums.ContentType"] = [
            enums.ContentType.SERIES,
            enums.ContentType.MOVIE,
            enums.ContentType.EPISODE,
            enums.ContentType.MUSIC,
        ],
        ratings: bool | None = True,
        start: int | None = None,
        preferred_audio_language: str | None = None,
        locale: str | None = None,
    ) -> types.BrowseQuery:
        """
        Browse for series, movies or episodes.

        Parameters:
            sort_by (``str``, *optional*):
                Sort content by criteria.
                Default to "newly_added".
            max_results (``int``, *optional*):
                Max results for every content type.
                Default to 36.
            filters (List of :obj:`~crunpyroll.enums.ContentType`, *optional*):
                Content types to filter by.
                Default to all content types.
            ratings (``bool``, *optional*):
                Include ratings in the response.
                Default to True.
            start (``int``, *optional*):
                Starting index for pagination.
                Default to None.
            preferred_audio_language (``str``, *optional*):
                Audio language request for different results.
                Default to the one used in Client.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`~crunpyroll.types.BrowseQuery`:
                On success, query of results is returned.
        """
        await self.session.retrieve()

        response = await self.download_browse(
            max_results=max_results,
            filters=filters,
            sort_by=sort_by,
            preferred_audio_language=preferred_audio_language,
            locale=locale,
            ratings=ratings,
            start=start,
        )

        return types.BrowseQuery.parse(response)
