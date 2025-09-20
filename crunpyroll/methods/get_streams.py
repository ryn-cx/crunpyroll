from crunpyroll import types
from crunpyroll import enums
from typing import Any
import crunpyroll


class GetStreams:
    async def download_streams(
        self: "crunpyroll.Client",  # type: ignore[reportGeneralTypeIssues]
        media_id: str,
        *,
        locale: str | None = None,
    ) -> dict[Any, Any]:
        """
        Download available streams of a media.

        Parameters:
            media_id (``str``):
                Unique identifier of the media.
            locale (``str``, *optional*):
                Localize request for different results.
                Default to the one used in Client.

        Returns:
            :obj:`dict`:
                Raw response data from the API.
        """
        await self.session.retrieve()
        response = await self.api_request(
            method="GET",
            endpoint="v1/" + media_id + "/android/phone/play",
            params={"locale": locale or self.locale, "queue": False},
            host=enums.APIHost.PLAY_SERVICE,
        )

        if response is None:
            raise ValueError("Failed to download streams.")

        return response

    async def get_streams(
        self: "crunpyroll.Client",  # type: ignore[reportGeneralTypeIssues]
        media_id: str,
        *,
        locale: str | None = None,
    ) -> types.MediaStreams:
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
        return types.MediaStreams.parse(response, media_id)
