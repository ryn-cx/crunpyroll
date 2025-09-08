from crunpyroll import types
from crunpyroll import enums

import crunpyroll

class GetLicense:
    async def download_license(
        self: "crunpyroll.Client",
        media_id: str,
        *,
        challenge: bytes,
        token: str,
    ) -> str:
        """
        Download DRM license data.

        .. todo::
            
            Add support for PlayReady DRM

        Parameters:
            media_id (``str``):
                Unique identifier of a media.
            challenge (``bytes``):
                Challenge provided by CDM.
            token (``str``):
                Token of the stream.

        Returns:
            ``str``:
                Raw license data.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="POST",
            endpoint="v1/license/widevine",
            params={"specConform": True},
            headers={
                "Content-Type": "application/octet-stream",
                "X-Cr-Content-Id": media_id,
                "X-Cr-Video-Token": token,
            },
            host=enums.APIHost.LICENSE,
            payload=challenge,
        )
        return response

    def parse_license(
        self: "crunpyroll.Client",
        response: str
    ) -> str:
        """
        Parse license data.

        Parameters:
            response (``str``):
                Raw license data.
                
        Returns:
            ``str``:
                Parsed license.
        """
        return response

    async def get_license(
        self: "crunpyroll.Client",
        media_id: str,
        *,
        challenge: bytes,
        token: str,
    ) -> str:
        """
        Get DRM license. Useful to obtain decryption keys.

        .. todo::
            
            Add support for PlayReady DRM

        Parameters:
            media_id (``str``):
                Unique identifier of a media.
            challenge (``bytes``):
                Challenge provided by CDM.
            token (``str``):
                Token of the stream.

        Returns:
            ``str``:
                On success, license is returned.
        """
        response = await self.download_license(media_id, challenge=challenge, token=token)
        return self.parse_license(response)