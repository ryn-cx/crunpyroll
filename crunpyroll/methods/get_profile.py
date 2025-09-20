from crunpyroll import types
from typing import Any
import crunpyroll


class GetProfile:
    async def download_profile(
        self: "crunpyroll.Client",  # type: ignore[reportGeneralTypeIssues]
    ) -> dict[Any, Any]:
        """
        Download current profile informations.

        Returns:
            :obj:`dict`:
                Raw response data from the API.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="accounts/v1/me/profile",
        )

        if response is None:
            raise ValueError("Failed to download profile.")

        return response

    async def get_profile(
        self: "crunpyroll.Client",  # type: ignore[reportGeneralTypeIssues]
    ) -> types.Profile:
        """
        Get current profile informations.

        Returns:
            :obj:`~crunpyroll.types.Profile`:
                On success, profile object is returned.
        """
        response = await self.download_profile()
        return types.Profile(response)
