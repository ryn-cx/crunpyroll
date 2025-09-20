from .browse import Browse
from .search import Search
from .get_index import GetIndex
from .get_profile import GetProfile
from .get_series import GetSeries
from .get_seasons import GetSeasons
from .get_episodes import GetEpisodes
from .get_objects import GetObjects
from .get_streams import GetStreams
from .get_manifest import GetManifest
from .get_license import GetLicense
from .delete_active_stream import DeleteActiveStream


class Methods(
    Browse,
    Search,
    GetIndex,
    GetProfile,
    GetSeries,
    GetSeasons,
    GetEpisodes,
    GetStreams,
    GetManifest,
    GetLicense,
    GetObjects,
    DeleteActiveStream,
):
    pass
