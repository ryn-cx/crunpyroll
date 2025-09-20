from datetime import datetime, timedelta

from .utils import get_date

from .errors import ClientNotAuthorized


import crunpyroll


class Session:
    def __init__(self, client: "crunpyroll.Client"):
        self._client = client

        self.access_token: str | None = None
        self.refresh_token: str | None = None
        self.expiration: datetime | None = None

    @property
    def is_authorized(self) -> bool:
        if self._client.anonymous:
            return bool(self.access_token)

        return bool(self.access_token and self.refresh_token)

    @property
    def authorization_header(self):
        return {"Authorization": f"Bearer {self.access_token}"}

    async def retrieve(self) -> None:
        if not self.is_authorized:
            raise ClientNotAuthorized("Client is not authorized yet.")
        date = get_date()
        if date >= self.expiration:
            await self.refresh()

    async def authorize(self) -> bool | None:
        if self._client.anonymous:
            response = await self._client.api_request(
                method="POST",
                endpoint="auth/v1/token",
                headers={"Authorization": f"Basic {self._client.public_token}"},
                payload={
                    "grant_type": "client_id",
                },
                include_session=False,
            )
        else:
            response = await self._client.api_request(
                method="POST",
                endpoint="auth/v1/token",
                headers={"Authorization": f"Basic {self._client.public_token}"},
                payload={
                    "username": self._client.email,
                    "password": self._client.password,
                    "grant_type": "password",
                    "scope": "offline_access",
                    "device_id": self._client.device_id,
                    "device_name": self._client.device_name,
                    "device_type": self._client.device_type,
                },
                include_session=False,
            )
            self.refresh_token = response.get("refresh_token")

        self.access_token = response.get("access_token")
        self.expiration = get_date() + timedelta(seconds=response.get("expires_in"))
        return True

    async def refresh(self) -> bool | None:
        if self._client.anonymous:
            response = await self._client.api_request(
                method="POST",
                endpoint="auth/v1/token",
                headers={"Authorization": f"Basic {self._client.public_token}"},
                payload={
                    "grant_type": "client_id",
                },
                include_session=False,
            )
        else:
            response = await self._client.api_request(
                method="POST",
                endpoint="auth/v1/token",
                headers={"Authorization": f"Basic {self._client.public_token}"},
                payload={
                    "refresh_token": self.refresh_token,
                    "grant_type": "refresh_token",
                    "scope": "offline_access",
                    "device_id": self._client.device_id,
                    "device_name": self._client.device_name,
                    "device_type": self._client.device_type,
                },
                include_session=False,
            )
            self.refresh_token = response.get("refresh_token")
        self.access_token = response.get("access_token")
        self.expiration = get_date() + timedelta(seconds=response.get("expires_in"))
        return True
