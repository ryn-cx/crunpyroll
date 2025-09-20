from typing import Any
from datetime import datetime, UTC
from uuid import uuid4


APP_VERSION = "3.59.0"

DEVICE_NAME = "RMX2170"
DEVICE_TYPE = "realme RMX2170"
DEVICE_ID = str(uuid4())

WIDEVINE_UUID = "urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed"
PLAYREADY_UUID = "urn:uuid:9a04f079-9840-4286-ab92-e65be0885f95"


def get_api_headers(headers: dict[Any, Any] | None) -> dict[Any, Any]:
    return {
        "Connection": "Keep-Alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": f"Crunchyroll/{APP_VERSION} Android/13 okhttp/4.12.0",
    } | (headers or {})


def parse_segments(repr: dict[Any, Any], template: dict[Any, Any]) -> list[str]:
    time = 0
    segments = []
    base_url = repr["BaseURL"]
    representation_id = repr["@id"]
    start_number = int(template["@startNumber"])
    initialization_url = format_segment_url(
        url=base_url + template["@initialization"],
        obj={"RepresentationID": representation_id},
    )
    segments.append(initialization_url)
    for segment in template["SegmentTimeline"]["S"]:
        repeat = int(segment.get("@r", 0)) + 1
        duration = int(segment.get("@d"))
        time += repeat * duration
        for _ in range(repeat):
            number = start_number + len(segments) - 1
            segment_url = format_segment_url(
                url=base_url + template["@media"],
                obj={"Number": str(number), "RepresentationID": representation_id},
            )
            segments.append(segment_url)
    return segments


def format_segment_url(url: str, obj: dict[Any, Any]) -> str:
    for key, value in obj.items():
        url = url.replace(f"${key}$", value)
    return url


def get_date() -> datetime:
    return datetime.now(UTC)


def date_to_str(date: datetime) -> str | None:
    try:
        return "{}-{}-{}T{}:{}:{}Z".format(
            date.year, date.month, date.day, date.hour, date.minute, date.second
        )
    except Exception:
        return


def str_to_date(string: str) -> datetime | None:
    formats = ["%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z"]

    for fmt in formats:
        try:
            return datetime.strptime(string, fmt)
        except ValueError:
            continue

    return None
