from crunpyroll import types
from crunpyroll import enums
from typing import Any

import crunpyroll


class GetStreams:
    async def download_streams(
        self: "crunpyroll.Client",
        media_id: str,
        *,
        locale: str = None,
    ) -> dict[str, Any]:
        """
        Download streams data of a media.

        Parameters:
            media_id (``str``):
                Unique identifier of the media.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            ``dict``:
                Raw API response data.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="v1/" + media_id + "/android/phone/play",
            params={"locale": locale or self.locale, "queue": False},
            host=enums.APIHost.PLAY_SERVICE,
        )
        return response

    def parse_streams(
        self: "crunpyroll.Client", response: dict, media_id: str
    ) -> "types.MediaStreams":
        """
        Parse streams data into MediaStreams object.

        Parameters:
            response (``dict``):
                Raw API response data.
            media_id (``str``):
                Unique identifier of the media.

        Returns:
            :obj:`~crunpyroll.types.MediaStreams`:
                Parsed media streams object.
        """
        return types.MediaStreams.parse(response, media_id)

    async def get_streams(
        self: "crunpyroll.Client",
        media_id: str,
        *,
        locale: str = None,
    ) -> "types.MediaStreams":
        """
        Get available streams of a media.

        Parameters:
            media_id (``str``):
                Unique identifier of the media.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`~crunpyroll.types.MediaStreams`:
                On success, streams are returned.
        """
        response = await self.download_streams(media_id, locale=locale)
        return self.parse_streams(response, media_id)
