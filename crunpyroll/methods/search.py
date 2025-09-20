from crunpyroll import enums
from crunpyroll import types
from typing import Any

import crunpyroll


class Search:
    async def download_search(
        self: "crunpyroll.Client",  # type: ignore[reportGeneralTypeIssues]
        query: str,
        *,
        max_results: int = 6,
        locale: str | None = None,
        filters: list[enums.ContentType] = [
            enums.ContentType.SERIES,
            enums.ContentType.MOVIE,
            enums.ContentType.EPISODE,
            enums.ContentType.MUSIC,
        ],
    ) -> dict[Any, Any]:
        """
        Download search for series, movies or episodes.

        Parameters:
            query (``str``):
                Query string to search.
            max_results (``int``, *optional*):
                Max results for every content type.
                Default to 6
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.
            filters (List of :obj:`~crunpyroll.enums.ContentType`, *optional*):
                Content to filters.
                Default to every value in :obj:`~crunpyroll.enums.ContentType`.

        Returns:
            :obj:`dict`:
                Raw response data from the API.
        """
        await self.session.retrieve()
        # TODO: Are the types trustworthy enough where isinstance can be removed?
        filters_string = ",".join(
            filter.value for filter in filters if isinstance(filter, enums.ContentType)
        )
        response = await self.api_request(
            method="GET",
            endpoint="content/v2/discover/search",
            params={
                "q": query,
                "n": max_results,
                "locale": locale or self.locale,
                "type": filters_string,
            },
        )

        if response is None:
            raise ValueError("Failed to download search results.")

        return response

    async def search(
        self: "crunpyroll.Client",  # type: ignore[reportGeneralTypeIssues]
        query: str,
        *,
        max_results: int = 6,
        locale: str | None = None,
        filters: list[enums.ContentType] = [
            enums.ContentType.SERIES,
            enums.ContentType.MOVIE,
            enums.ContentType.EPISODE,
            enums.ContentType.MUSIC,
        ],
    ) -> types.SearchQuery:
        """
        Search for series, movies or episodes.

        Parameters:
            query (``str``):
                Query string to search.
            max_results (``int``, *optional*):
                Max results for every content type.
                Default to 6
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.
            filters (List of :obj:`~crunpyroll.enums.ContentType`, *optional*):
                Content to filters.
                Default to every value in :obj:`~crunpyroll.enums.ContentType`.

        Returns:
            :obj:`~crunpyroll.types.SearchQuery`:
                On success, query of results is returned.
        """
        response = await self.download_search(query, max_results=max_results, locale=locale, filters=filters)
        return types.SearchQuery.parse(response)
