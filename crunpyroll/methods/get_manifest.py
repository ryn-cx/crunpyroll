from crunpyroll import types

import crunpyroll

class GetManifest:
    async def download_manifest(
        self: "crunpyroll.Client",
        url: str
    ) -> str:
        """
        Download manifest data.

        Parameters:
            url (``str``):
                URL of the manifest.

        Returns:
            ``str``:
                Raw manifest data.
        """
        await self.session.retrieve()
        response = await self.manifest_request(url)
        return response

    def parse_manifest(
        self: "crunpyroll.Client",
        response: str
    ) -> "types.Manifest":
        """
        Parse manifest data into Manifest object.

        Parameters:
            response (``str``):
                Raw manifest data.
                
        Returns:
            :obj:`~crunpyroll.types.Manifest`:
                Parsed manifest object.
        """
        return types.Manifest.parse(response)

    async def get_manifest(
        self: "crunpyroll.Client",
        url: str
    ) -> "types.Manifest":
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
        return self.parse_manifest(response)