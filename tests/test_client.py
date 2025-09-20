import crunpyroll
import pytest
from pathlib import Path
from crunpyroll import types
import json

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_start_client():
    client = crunpyroll.Client()
    await client.start()


@pytest.mark.asyncio
async def test_episodes_endpoint():
    output_path = Path("tests/data/episodes/GY8VCP4J2.json")
    if not output_path.exists():
        client = crunpyroll.Client()
        await client.start()
        response = await client.download_episodes("GY8VCP4J2")

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(response, indent=2))

    types.EpisodesQuery.parse(json.loads(output_path.read_text()))


@pytest.mark.asyncio
async def test_seasons_endpoint():
    output_path = Path("tests/data/seasons/GRMG8ZQZR.json")
    if not output_path.exists():
        client = crunpyroll.Client()
        await client.start()
        response = await client.download_seasons("GRMG8ZQZR")

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(response, indent=2))

    types.SeasonsQuery.parse(json.loads(output_path.read_text()))


@pytest.mark.asyncio
async def test_objects_endpoint():
    output_path = Path("tests/data/objects/GRJQC1E51.json")
    if not output_path.exists():
        client = crunpyroll.Client()
        await client.start()
        response = await client.download_objects("GRJQC1E51")

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(response, indent=2))

    types.ObjectsQuery.parse(json.loads(output_path.read_text()))


@pytest.mark.asyncio
async def test_session_index_endpoint():
    output_path = Path("tests/data/session_index/index.json")
    if not output_path.exists():
        client = crunpyroll.Client()
        await client.start()
        response = await client.download_index()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(response, indent=2))

    types.SessionIndex(json.loads(output_path.read_text()))


@pytest.mark.asyncio
async def test_series_endpoint():
    output_path = Path("tests/data/series/GY5P48XEY.json")
    if not output_path.exists():
        client = crunpyroll.Client()
        await client.start()
        response = await client.download_series("GY5P48XEY")

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(response, indent=2))

    types.Series.parse(json.loads(output_path.read_text()))


@pytest.mark.asyncio
async def test_search_endpoint():
    output_path = Path("tests/data/search/Demon Slayer.json")
    if not output_path.exists():
        client = crunpyroll.Client()
        await client.start()
        response = await client.download_search("Demon Slayer")

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(response, indent=2))

    types.SearchQuery.parse(json.loads(output_path.read_text()))


@pytest.mark.asyncio
async def test_browse_endpoint():
    output_path = Path("tests/data/browse/browse.json")
    if not output_path.exists():
        client = crunpyroll.Client()
        await client.start()
        response = await client.download_browse()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(response, indent=2))

    types.BrowseQuery.parse(json.loads(output_path.read_text()))
