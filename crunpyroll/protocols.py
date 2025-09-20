from typing import Protocol, Any
from .session import Session
from .enums import APIHost
import httpx


class ClientProtocol(Protocol):
    """Protocol defining the interface that all method classes expect from the Client."""

    session: Session
    locale: str
    http: httpx.AsyncClient

    async def api_request(
        self,
        method: str,
        endpoint: str,
        host: APIHost = APIHost.BETA,
        url: str | None = None,
        params: dict[Any, Any] | None = None,
        headers: dict[Any, Any] | None = None,
        payload: dict[Any, Any] | None = None,
        include_session: bool = True,
    ) -> dict[Any, Any] | None:
        ...

    async def manifest_request(
        self,
        url: str,
        headers: dict[Any, Any] | None = None,
    ) -> str:
        ...