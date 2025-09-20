from crunpyroll import types
from crunpyroll.protocols import ClientProtocol
from typing import Any


class GetIndex(ClientProtocol):
    async def download_index(self) -> dict[Any, Any]:
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

    async def get_index(self) -> types.SessionIndex:
        """
        Get session index. It's unlikely that you would use this method.

        Returns:
            :obj:`~crunpyroll.types.SessionIndex`:
                On success, informations about session index are returned.
        """
        response = await self.download_index()
        return types.SessionIndex(response)
