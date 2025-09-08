from crunpyroll import types

import crunpyroll

class GetProfile:
    async def download_profile(
        self: "crunpyroll.Client",
    ) -> dict:
        """
        Download current profile data.

        Returns:
            ``dict``:
                Raw API response data.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="accounts/v1/me/profile",
        )
        return response

    def parse_profile(
        self: "crunpyroll.Client",
        response: dict
    ) -> "types.Profile":
        """
        Parse profile data into Profile object.

        Parameters:
            response (``dict``):
                Raw API response data.
                
        Returns:
            :obj:`~crunpyroll.types.Profile`:
                Parsed profile object.
        """
        return types.Profile(response)

    async def get_profile(
        self: "crunpyroll.Client",
    ) -> "types.Profile":
        """
        Get current profile informations.

        Returns:
            :obj:`~crunpyroll.types.Profile`:
                On success, profile object is returned.
        """
        response = await self.download_profile()
        return self.parse_profile(response)