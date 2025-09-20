import crunpyroll
import pytest
from pathlib import Path
import json

pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_start_client():
    client = crunpyroll.Client()
    await client.start()


@pytest.mark.asyncio
async def test_get_episode():
    client = crunpyroll.Client()
    await client.start()
    episodes = await client.get_episodes("GRJQC1E51")
    dumped_episode = json.loads(str(episodes.items[0]))

    expected_values_path = Path("tests/data/episode.json")
    expected_values_parsed = json.loads(expected_values_path.read_text())
    # Go through each value and make sure they match, if any value doesn't match that
    # means that something in the API format has changed or the data has changed, either
    # way the difference should be investigated.
    for actual, expected in zip(dumped_episode, expected_values_parsed):
        assert actual == expected
