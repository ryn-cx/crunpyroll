import crunpyroll
import pytest
from .secrets import USERNAME, PASSWORD, DEVICE_ID

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