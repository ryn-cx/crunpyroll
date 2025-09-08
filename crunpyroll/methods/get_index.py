from crunpyroll import types

import crunpyroll

class GetIndex:
    async def download_index(
        self: "crunpyroll.Client",
    ) -> dict:
        """
        Download session index data.

        Returns:
            ``dict``:
                Raw API response data.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="index/v2",
        )
        return response

    def parse_index(
        self: "crunpyroll.Client",
        response: dict
    ) -> "types.SessionIndex":
        """
        Parse index data into SessionIndex object.

        Parameters:
            response (``dict``):
                Raw API response data.
                
        Returns:
            :obj:`~crunpyroll.types.SessionIndex`:
                Parsed session index object.
        """
        return types.SessionIndex(response)

    async def get_index(
        self: "crunpyroll.Client",
    ) -> "types.SessionIndex":
        """
        Get session index. It's unlikely that you would use this method.

        Returns:
            :obj:`~crunpyroll.types.SessionIndex`:
                On success, informations about session index are returned.
        """
        response = await self.download_index()
        return self.parse_index(response)