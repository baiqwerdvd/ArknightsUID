import asyncio
from pathlib import Path
import json
import threading

from ..utils.resource.download_all_resource import download_all_resource
from ..utils.resource.RESOURCE_PATH import GAMEDATA_PATH
from ..utils.models.gamedata.BattleEquipTable import BattleEquipTable
from ..utils.models.gamedata.BuildingData import BuildingData
from ..utils.models.gamedata.CampaignTable import CampaignTable
from ..utils.models.gamedata.ChapterTable import ChapterTable
from ..utils.models.gamedata.CharacterTable import CharacterTable
from ..utils.models.gamedata.CharMetaTable import CharMetaTable
from ..utils.models.gamedata.CharmTable import CharmTable
from ..utils.models.gamedata.CharPatchTable import CharPatchTable
from ..utils.models.gamedata.CharwordTable import CharwordTable
from ..utils.models.gamedata.CheckinTable import CheckinTable
from ..utils.models.gamedata.ClimbTowerTable import ClimbTowerTable
from ..utils.models.gamedata.ClueData import ClueData
from ..utils.models.gamedata.CrisisTable import CrisisTable
from ..utils.models.gamedata.CrisisV2Table import CrisisV2Table
from ..utils.models.gamedata.EnemyHandbookTable import EnemyHandbookTable
from ..utils.models.gamedata.FavorTable import FavorTable
from ..utils.models.gamedata.GachaTable import GachaTable
from ..utils.models.gamedata.GamedataConst import GamedataConst
from ..utils.models.gamedata.HandbookInfoTable import HandbookInfoTable
from ..utils.models.gamedata.HandbookTable import HandbookTable
from ..utils.models.gamedata.HandbookTeamTable import HandbookTeamTable
from ..utils.models.gamedata.MedalTable import MedalTable
from ..utils.models.gamedata.MissionTable import MissionTable
from ..utils.models.gamedata.OpenServerTable import OpenServerTable
from ..utils.models.gamedata.PlayerAvatarTable import PlayerAvatarTable
from ..utils.models.gamedata.RangeTable import RangeTable
from ..utils.models.gamedata.ReplicateTable import ReplicateTable
from ..utils.models.gamedata.RetroTable import RetroTable
from ..utils.models.gamedata.RoguelikeTable import RoguelikeTable
from ..utils.models.gamedata.RoguelikeTopicTable import RoguelikeTopicTable
from ..utils.models.gamedata.SandboxTable import SandboxTable
from ..utils.models.gamedata.ShopClientTable import ShopClientTable
from ..utils.models.gamedata.SkillTable import SkillTable
from ..utils.models.gamedata.SkinTable import SkinTable
from ..utils.models.gamedata.StageTable import StageTable
from ..utils.models.gamedata.StoryReviewMetaTable import StoryReviewMetaTable
from ..utils.models.gamedata.StoryReviewTable import StoryReviewTable
from ..utils.models.gamedata.StoryTable import StoryTable
from ..utils.models.gamedata.TechBuffTable import TechBuffTable
from ..utils.models.gamedata.TipTable import TipTable
from ..utils.models.gamedata.TokenTable import TokenTable
from ..utils.models.gamedata.UniequipData import UniequipData
from ..utils.models.gamedata.UniequipTable import UniEquipTable
from ..utils.models.gamedata.ZoneTable import ZoneTable

from gsuid_core.logger import logger


def read_json(file_path: Path, **kwargs) -> dict:
    """
    Read a JSON file and return its contents as a dictionary.
    """
    try:
        with Path.open(file_path, encoding="UTF-8", **kwargs) as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading JSON file: {e}")
        return {}


threading.Thread(target=lambda: asyncio.run(download_all_resource()), daemon=True).start()
# ACTIVITY_TABLE = ActivityTable.convert(read_json(GAMEDATA_PATH / 'activity_table.json'))
# AUDIO_DATA = AudioData.convert(read_json(GAMEDATA_PATH / 'audio_data.json'))

BATTLE_EQUIP_TABLE = BattleEquipTable.convert(
    {"equips": read_json(GAMEDATA_PATH / "battle_equip_table.json")}
)
BUILDING_DATA = BuildingData.convert(read_json(GAMEDATA_PATH / "building_data.json"))

CAMPAIGN_TABLE = CampaignTable.convert(read_json(GAMEDATA_PATH / "campaign_table.json"))
CHAPTER_TABLE = ChapterTable.convert(
    {"chapters": read_json(GAMEDATA_PATH / "chapter_table.json")}
)
CHARACTER_TABLE = CharacterTable.convert(
    {"chars": read_json(GAMEDATA_PATH / "character_table.json")}
)
CHAR_META_TABLE = CharMetaTable.convert(read_json(GAMEDATA_PATH / "char_meta_table.json"))
CHARM_TABLE = CharmTable.convert(read_json(GAMEDATA_PATH / "charm_table.json"))
CHAR_PATH_TABLE = CharPatchTable.convert(read_json(GAMEDATA_PATH / "char_patch_table.json"))
CHARWORD_TABLE = CharwordTable.convert(read_json(GAMEDATA_PATH / "charword_table.json"))
CHECKIN_TABLE = CheckinTable.convert(read_json(GAMEDATA_PATH / "checkin_table.json"))
CLIMB_TOWER_TABLE = ClimbTowerTable.convert(read_json(GAMEDATA_PATH / "climb_tower_table.json"))
CLUE_DATA = ClueData.convert(read_json(GAMEDATA_PATH / "clue_data.json"))
CRISIS_TABLE = CrisisTable.convert(read_json(GAMEDATA_PATH / "crisis_table.json"))
CRISIS_V2_TABLE = CrisisV2Table.convert(read_json(GAMEDATA_PATH / "crisis_v2_table.json"))

# DISPLAY_META_TABLE = DisplayMetaTable.convert(read_json(GAMEDATA_PATH / 'display_meta_table.json'))

ENEMY_HANDBOOK_TABLE = EnemyHandbookTable.convert(
    read_json(GAMEDATA_PATH / "enemy_handbook_table.json")
)

FAVOR_TABLE = FavorTable.convert(read_json(GAMEDATA_PATH / "favor_table.json"))

GACHA_TABLE = GachaTable.convert(read_json(GAMEDATA_PATH / "gacha_table.json"))
GAMEDATA_CONST = GamedataConst.convert(read_json(GAMEDATA_PATH / "gamedata_const.json"))

HANDBOOK_INFO_TABLE = HandbookInfoTable.convert(
    read_json(GAMEDATA_PATH / "handbook_info_table.json")
)
HANDBOOK_TABLE = HandbookTable.convert(read_json(GAMEDATA_PATH / "handbook_table.json"))
HANDBOOK_TEAM_TABLE = HandbookTeamTable.convert(
    {"team": read_json(GAMEDATA_PATH / "handbook_team_table.json")}
)

# ITEM_TABLE = ItemTable.convert(read_json(GAMEDATA_PATH / "item_table.json"))

MEDAL_TABLE = MedalTable.convert(read_json(GAMEDATA_PATH / "medal_table.json"))
MISSION_TABLE = MissionTable.convert(read_json(GAMEDATA_PATH / "mission_table.json"))

OPEN_SERVER_TABLE = OpenServerTable.convert(read_json(GAMEDATA_PATH / "open_server_table.json"))

PLAYER_AVATAR_TABLE = PlayerAvatarTable.convert(
    read_json(GAMEDATA_PATH / "player_avatar_table.json")
)

RANGE_TABLE = RangeTable.convert({"range_": read_json(GAMEDATA_PATH / "range_table.json")})
REPLICATE_TABLE = ReplicateTable.convert(
    {"replicate": read_json(GAMEDATA_PATH / "replicate_table.json")}
)
RETRO_TABLE = RetroTable.convert(read_json(GAMEDATA_PATH / "retro_table.json"))
ROGUELIKE_TABLE = RoguelikeTable.convert(read_json(GAMEDATA_PATH / "roguelike_table.json"))
ROGUELIKE_TOPIC_TABLE = RoguelikeTopicTable.convert(
    read_json(GAMEDATA_PATH / "roguelike_topic_table.json")
)

SANDBOX_TABLE = SandboxTable.convert(read_json(GAMEDATA_PATH / "sandbox_table.json"))
# SANDBOX_PERM_TABLE = SandboxPermTable.convert(
#     read_json(GAMEDATA_PATH / "sandbox_perm_table.json")
# )
SHOP_CLIENT_TABLE = ShopClientTable.convert(read_json(GAMEDATA_PATH / "shop_client_table.json"))
SKILL_TABLE = SkillTable.convert(
    {"skills": read_json(Path(__file__).parent / "skill_table.json")}
)
SKIN_TABLE = SkinTable.convert(read_json(GAMEDATA_PATH / "skin_table.json"))
STAGE_TABLE = StageTable.convert(read_json(GAMEDATA_PATH / "stage_table.json"))
STORY_REVIEW_META_TABLE = StoryReviewMetaTable.convert(
    read_json(GAMEDATA_PATH / "story_review_meta_table.json")
)
STORY_REVIEW_TABLE = StoryReviewTable.convert(
    {"storyreviewtable": read_json(GAMEDATA_PATH / "story_review_table.json")}
)
STORY_TABLE = StoryTable.convert({"stories": read_json(GAMEDATA_PATH / "story_table.json")})

TECH_BUFF_TABLE = TechBuffTable.convert(read_json(GAMEDATA_PATH / "tech_buff_table.json"))
TIP_TABLE = TipTable.convert(read_json(GAMEDATA_PATH / "tip_table.json"))
TOKEN_TABLE = TokenTable.convert({"tokens": read_json(GAMEDATA_PATH / "token_table.json")})

UNIEQUIP_DATA = UniequipData.convert(read_json(GAMEDATA_PATH / "uniequip_data.json"))
UNIEQUIP_TABLE = UniEquipTable.convert(read_json(GAMEDATA_PATH / "uniequip_table.json"))
ZONE_TABLE = ZoneTable.convert(read_json(GAMEDATA_PATH / "zone_table.json"))
