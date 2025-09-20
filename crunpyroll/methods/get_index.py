from crunpyroll import types
from typing import Any
import crunpyroll


class GetIndex:
    async def download_index(
        self: "crunpyroll.Client",  # type: ignore[reportGeneralTypeIssues]
    ) -> dict[Any, Any]:
        """
        Download session index.

        Returns:
            :obj:`dict`:
                Raw response data from the API.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="index/v2",
        )

        if response is None:
            raise ValueError("Failed to download index.")

        return response

    async def get_index(
        self: "crunpyroll.Client",  # type: ignore[reportGeneralTypeIssues]
    ) -> types.SessionIndex:
        """
        Get session index. It's unlikely that you would use this method.

        Returns:
            :obj:`~crunpyroll.types.SessionIndex`:
                On success, informations about session index are returned.
        """
        response = await self.download_index()
        return types.SessionIndex(response)
