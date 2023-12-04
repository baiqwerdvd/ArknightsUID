from gsuid_core.utils.download_resource.download_core import download_all_file

from .RESOURCE_PATH import GAMEDATA_PATH


async def download_all_file_from_cos():
    await download_all_file(
        'ArknightsUID',
        {
            'resource/gamedata': GAMEDATA_PATH,
        },
    )
