from crunpyroll import types
from typing import Any
import crunpyroll


class GetManifest:
    async def download_manifest(
        self: "crunpyroll.Client",  # type: ignore[reportGeneralTypeIssues]
        url: str,
    ) -> str:
        """
        Retrieve manifest.

        Parameters:
            url (``str``):
                URL of the manifest.

        Returns:
            :obj:`str`:
                Raw manifest data.

        """
        await self.session.retrieve()
        return await self.manifest_request(url)

    async def get_manifest(
        self: "crunpyroll.Client",  # type: ignore[reportGeneralTypeIssues]
        url: str,
    ) -> types.Manifest:
        """
        Retrieve and parse manifest.

        Parameters:
            url (``str``):
                URL of the manifest.

        Returns:
            :obj:`~crunpyroll.types.Manifest`:
                On success, parsed manifest is returned.

        """
        response = await self.download_manifest(url)
        return types.Manifest.parse(response)
