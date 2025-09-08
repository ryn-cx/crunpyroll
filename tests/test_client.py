import crunpyroll
import pytest
from .secrets import USERNAME, PASSWORD, DEVICE_ID
from pathlib import Path
import json
pytest_plugins = ('pytest_asyncio',)

client = crunpyroll.Client(
    email=USERNAME,
    password=PASSWORD,
    locale="en-US",
    device_id=DEVICE_ID,
)

@pytest.mark.asyncio
async def test_start_client():
    await client.start()

# This only tests the first episode but it's good enough for being notified if the API
# format changes.
@pytest.mark.asyncio
async def test_episode():
    await client.start()
    episodes = await client.get_episodes("GRJQC1E51")
    dumped_episode = json.loads(str(episodes.items[0]))
    
    expected_values_path = Path("tests/data/episode.json")
    expected_values_parsed = json.loads(expected_values_path.read_text())

    for actual, expected in zip(dumped_episode, expected_values_parsed):
        assert actual == expected
