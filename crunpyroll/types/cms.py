from ..utils import str_to_date

from .obj import Object

from typing import Any


class CMS(Object):
    """
    Content Management System for Crunchyroll.

    Parameters:
        bucket (``str``)

        policy (``str``)

        signature (``str``)

        key_pair_id (``str``)

        expires (:py:obj:`~datetime.datetime`)
    """

    def __init__(self, data: dict[Any, Any]):
        self.bucket: str = data.get("bucket")
        self.policy: str = data.get("policy")
        self.signature: str = data.get("signature")
        self.key_pair_id: str = data.get("key_pair_id")
        self.expires = str_to_date(data.get("expires"))
