import inspect
from typing import Dict, Union
from msgspec import json as msgjson

from ..utils.models.gamedata.ActivityTable import ActivityTable
from ..utils.models.gamedata.AudioData import AudioData
from ..utils.models.gamedata.BattleEquipTable import BattleEquipData
from ..utils.models.gamedata.BuildingData import BuildingData
from ..utils.models.gamedata.CampaignTable import CampaignTable
from ..utils.models.gamedata.ChapterTable import ChapterData
from ..utils.models.gamedata.CharacterTable import CharacterData
from ..utils.models.gamedata.CharMetaTable import CharMetaTable
from ..utils.models.gamedata.CharmTable import CharmTable
from ..utils.models.gamedata.CharPatchTable import CharPatchTable
from ..utils.models.gamedata.CharwordTable import CharwordTable
from ..utils.models.gamedata.CheckinTable import CheckinTable
from ..utils.models.gamedata.ClimbTowerTable import ClimbTowerTable
from ..utils.models.gamedata.ClueData import ClueData
from ..utils.models.gamedata.CrisisTable import CrisisTable
from ..utils.models.gamedata.DisplayMetaTable import DisplayMetaTable
from ..utils.models.gamedata.EnemyHandbookTable import EnemyHandbookTable
from ..utils.models.gamedata.FavorTable import FavorTable
from ..utils.models.gamedata.GachaTable import GachaTable
from ..utils.models.gamedata.GamedataConst import GamedataConst
from ..utils.models.gamedata.HandbookInfoTable import HandbookInfoTable
from ..utils.models.gamedata.HandbookTable import HandbookTable
from ..utils.models.gamedata.HandbookTeamTable import HandbookTeam
from ..utils.models.gamedata.ItemTable import ItemTable
from ..utils.models.gamedata.MedalTable import MedalTable
from ..utils.models.gamedata.MissionTable import MissionTable
from ..utils.models.gamedata.OpenServerTable import OpenServerTable
from ..utils.models.gamedata.PlayerAvatarTable import PlayerAvatarTable
from ..utils.models.gamedata.RangeTable import Stage
from ..utils.models.gamedata.ReplicateTable import ReplicateList
from ..utils.models.gamedata.RetroTable import RetroTable
from ..utils.models.gamedata.RoguelikeTable import RoguelikeTable
from ..utils.models.gamedata.RoguelikeTopicTable import RoguelikeTopicTable
from ..utils.models.gamedata.SandboxTable import SandboxTable
from ..utils.models.gamedata.ShopClientTable import ShopClientTable
from ..utils.models.gamedata.SkillTable import SkillDataBundle
from ..utils.models.gamedata.SkinTable import SkinTable
from ..utils.models.gamedata.StageTable import StageTable
from ..utils.models.gamedata.StoryReviewMetaTable import StoryReviewMetaTable
from ..utils.models.gamedata.StoryReviewTable import StoryReviewGroupClientData
from ..utils.models.gamedata.StoryTable import StoryData
from ..utils.models.gamedata.TechBuffTable import TechBuffTable
from ..utils.models.gamedata.TipTable import TipTable
from ..utils.models.gamedata.TokenTable import TokenCharacterData
from ..utils.models.gamedata.UniequipData import UniequipData
from ..utils.models.gamedata.UniequipTable import UniEquipTable
from ..utils.models.gamedata.ZoneTable import ZoneTable
from .cachedata import CacheData


class ExcelTableManager:
    activity_table_: Union[ActivityTable, None] = None
    audio_data_: Union[AudioData, None] = None
    battle_equip_table_: Union[Dict[str, BattleEquipData], None] = None
    building_data_: Union[BuildingData, None] = None
    campaign_table_: Union[CampaignTable, None] = None
    chapter_table_: Union[Dict[str, ChapterData], None] = None
    character_table_: Union[Dict[str, CharacterData], None] = None
    char_meta_table_: Union[CharMetaTable, None] = None
    charm_table_: Union[CharmTable, None] = None
    char_patch_table_: Union[CharPatchTable, None] = None
    charword_table_: Union[CharwordTable, None] = None
    checkin_table_: Union[CheckinTable, None] = None
    climb_tower_table_: Union[ClimbTowerTable, None] = None
    clue_data_: Union[ClueData, None] = None
    crisis_table_: Union[CrisisTable, None] = None
    display_meta_table_: Union[DisplayMetaTable, None] = None
    enemy_handbook_table_: Union[EnemyHandbookTable, None] = None
    favor_table_: Union[FavorTable, None] = None
    gacha_table_: Union[GachaTable, None] = None
    gamedata_const_: Union[GamedataConst, None] = None
    handbook_info_table_: Union[HandbookInfoTable, None] = None
    handbook_table_: Union[HandbookTable, None] = None
    handbook_team_table_: Union[Dict[str, HandbookTeam], None] = None
    item_table_: Union[ItemTable, None] = None
    medal_table_: Union[MedalTable, None] = None
    mission_table_: Union[MissionTable, None] = None
    open_server_table_: Union[OpenServerTable, None] = None
    player_avatar_table_: Union[PlayerAvatarTable, None] = None
    range_table_: Union[Dict[str, Stage], None] = None
    replicate_table_: Union[Dict[str, ReplicateList], None] = None
    retro_table_: Union[RetroTable, None] = None
    roguelike_table_: Union[RoguelikeTable, None] = None
    roguelike_topic_table_: Union[RoguelikeTopicTable, None] = None
    sandbox_table_: Union[SandboxTable, None] = None
    shop_client_table_: Union[ShopClientTable, None] = None
    skill_table_: Union[Dict[str, SkillDataBundle], None] = None
    skin_table_: Union[SkinTable, None] = None
    stage_table_: Union[StageTable, None] = None
    story_review_meta_table_: Union[StoryReviewMetaTable, None] = None
    story_review_table_: Union[Dict[str, StoryReviewGroupClientData], None] = None
    story_table_: Union[Dict[str, StoryData], None] = None
    tech_buff_table_: Union[TechBuffTable, None] = None
    tip_table_: Union[TipTable, None] = None
    token_table_: Union[Dict[str, TokenCharacterData], None] = None
    uniequip_data_: Union[UniequipData, None] = None
    uniequip_table_: Union[UniEquipTable, None] = None
    zone_table_: Union[ZoneTable, None] = None

    @property
    def ACTIVITY_TABLE(self) -> ActivityTable:
        if not self.activity_table_:
            self.activity_table_ = ActivityTable.convert(
                CacheData.readExcel('activity_table')
            )
        return self.activity_table_

    @property
    def AUDIO_DATA(self) -> AudioData:
        if not self.audio_data_:
            self.audio_data_ = AudioData.convert(
                CacheData.readExcel('audio_data')
            )
        return self.audio_data_

    @property
    def BATTLE_EQUIP_TABLE(self) -> Dict[str, BattleEquipData]:
        if not self.battle_equip_table_:
            self.battle_equip_table_ = msgjson.decode(
                CacheData.readBytesExcel('battle_equip_table'),
                type=Dict[str, BattleEquipData]
            )
        return self.battle_equip_table_

    @property
    def BUILDING_DATA(self) -> BuildingData:
        if not self.building_data_:
            self.building_data_ = BuildingData.convert(
                CacheData.readExcel('building_data')
            )
        return self.building_data_

    @property
    def CAMPAIGN_TABLE(self) -> CampaignTable:
        if not self.campaign_table_:
            self.campaign_table_ = CampaignTable.convert(
                CacheData.readExcel('campaign_table')
            )
        return self.campaign_table_

    @property
    def CHAPTER_TABLE(self) -> Dict[str, ChapterData]:
        if not self.chapter_table_:
            self.chapter_table_ = msgjson.decode(
                CacheData.readBytesExcel('chapter_table'),
                type=Dict[str, ChapterData]
            )
        return self.chapter_table_

    @property
    def CHARATER_TABLE(self) -> Dict[str, CharacterData]:
        if not self.character_table_:
            self.character_table_ = msgjson.decode(
                CacheData.readBytesExcel('character_table'),
                type=Dict[str, CharacterData]
            )
        return self.character_table_

    @property
    def CHAR_META_TABLE(self) -> CharMetaTable:
        if not self.char_meta_table_:
            self.char_meta_table_ = CharMetaTable.convert(
                CacheData.readExcel('char_meta_table')
            )
        return self.char_meta_table_

    @property
    def CHARM_TABLE(self) -> CharmTable:
        if not self.charm_table_:
            self.charm_table_ = CharmTable.convert(
                CacheData.readExcel('charm_table')
            )
        return self.charm_table_

    @property
    def CHAR_PATH_TABLE(self) -> CharPatchTable:
        if not self.char_patch_table_:
            self.char_patch_table_ = CharPatchTable.convert(
                CacheData.readExcel('char_patch_table')
            )
        return self.char_patch_table_

    @property
    def CHARWORD_TABLE(self) -> CharwordTable:
        if not self.charword_table_:
            self.charword_table_ = CharwordTable.convert(
                CacheData.readExcel('charword_table')
            )
        return self.charword_table_

    @property
    def CHECKIN_TABLE(self) -> CheckinTable:
        if not self.checkin_table_:
            self.checkin_table_ = CheckinTable.convert(
                CacheData.readExcel('checkin_table')
            )
        return self.checkin_table_

    @property
    def CLIMB_TOWER_TABLE(self) -> ClimbTowerTable:
        if not self.climb_tower_table_:
            self.climb_tower_table_ = ClimbTowerTable.convert(
                CacheData.readExcel('climb_tower_table')
            )
        return self.climb_tower_table_

    @property
    def CLUE_DATA(self) -> ClueData:
        if not self.clue_data_:
            self.clue_data_ = ClueData.convert(
                CacheData.readExcel('clue_data')
            )
        return self.clue_data_

    @property
    def CRISIS_TABLE(self) -> CrisisTable:
        if not self.crisis_table_:
            self.crisis_table_ = CrisisTable.convert(
                CacheData.readExcel('crisis_table')
            )
        return self.crisis_table_

    @property
    def DISPLAY_META_TABLE(self) -> DisplayMetaTable:
        if not self.display_meta_table_:
            self.display_meta_table_ = DisplayMetaTable.convert(
                CacheData.readExcel('display_meta_table')
            )
        return self.display_meta_table_

    @property
    def ENEMY_HANDBOOK_TABLE(self) -> EnemyHandbookTable:
        if not self.enemy_handbook_table_:
            self.enemy_handbook_table_ = EnemyHandbookTable.convert(
                CacheData.readExcel('enemy_handbook_table')
            )
        return self.enemy_handbook_table_

    @property
    def FAVOR_TABLE(self) -> FavorTable:
        if not self.favor_table_:
            self.favor_table_ = FavorTable.convert(
                CacheData.readExcel('favor_table')
            )
        return self.favor_table_

    @property
    def GACHA_TABLE(self) -> GachaTable:
        if not self.gacha_table_:
            self.gacha_table_ = GachaTable.convert(
                CacheData.readExcel('gacha_table')
            )
        return self.gacha_table_

    @property
    def GAMEDATA_CONST(self) -> GamedataConst:
        if not self.gamedata_const_:
            self.gamedata_const_ = GamedataConst.convert(
                CacheData.readExcel('gamedata_const')
            )
        return self.gamedata_const_

    @property
    def HANDBOOK_INFO_TABLE(self) -> HandbookInfoTable:
        if not self.handbook_info_table_:
            self.handbook_info_table_ = HandbookInfoTable.convert(
                CacheData.readExcel('handbook_info_table')
            )
        return self.handbook_info_table_

    @property
    def HANDBOOK_TABLE(self) -> HandbookTable:
        if not self.handbook_table_:
            self.handbook_table_ = HandbookTable.convert(
                CacheData.readExcel('handbook_table')
            )
        return self.handbook_table_

    @property
    def HANDBOOK_TEAM_TABLE(self) -> Dict[str, HandbookTeam]:
        if not self.handbook_team_table_:
            self.handbook_team_table_ = msgjson.decode(
                CacheData.readBytesExcel('handbook_team_table'),
                type=Dict[str, HandbookTeam]
            )
        return self.handbook_team_table_

    @property
    def ITEM_TABLE(self) -> ItemTable:
        if not self.item_table_:
            self.item_table_ = ItemTable.convert(
                CacheData.readExcel('item_table')
            )
        return self.item_table_

    @property
    def MEDAL_TABLE(self) -> MedalTable:
        if not self.medal_table_:
            self.medal_table_ = MedalTable.convert(
                CacheData.readExcel('medal_table')
            )
        return self.medal_table_

    @property
    def MISSION_TABLE(self) -> MissionTable:
        if not self.mission_table_:
            self.mission_table_ = MissionTable.convert(
                CacheData.readExcel('mission_table')
            )
        return self.mission_table_

    @property
    def OPEN_SERVER_TABLE(self) -> OpenServerTable:
        if not self.open_server_table_:
            self.open_server_table_ = OpenServerTable.convert(
                CacheData.readExcel('open_server_table')
            )
        return self.open_server_table_

    @property
    def PLAYER_AVATAR_TABLE(self) -> PlayerAvatarTable:
        if not self.player_avatar_table_:
            self.player_avatar_table_ = PlayerAvatarTable.convert(
                CacheData.readExcel('player_avatar_table')
            )
        return self.player_avatar_table_

    @property
    def RANGE_TABLE(self) -> Dict[str, Stage]:
        if not self.range_table_:
            self.range_table_ = msgjson.decode(
                CacheData.readBytesExcel('range_table'),
                type=Dict[str, Stage]
            )
        return self.range_table_

    @property
    def REPLICATE_TABLE(self) -> Dict[str, ReplicateList]:
        if not self.replicate_table_:
            self.replicate_table_ = msgjson.decode(
                CacheData.readBytesExcel('replicate_table'),
                type=Dict[str, ReplicateList]
            )
        return self.replicate_table_

    @property
    def RETRO_TABLE(self) -> RetroTable:
        if not self.retro_table_:
            self.retro_table_ = RetroTable.convert(
                CacheData.readExcel('retro_table')
            )
        return self.retro_table_

    @property
    def ROGUELIKE_TABLE(self) -> RoguelikeTable:
        if not self.roguelike_table_:
            self.roguelike_table_ = RoguelikeTable.convert(
                CacheData.readExcel('roguelike_table')
            )
        return self.roguelike_table_

    @property
    def ROGUELIKE_TOPIC_TABLE(self) -> RoguelikeTopicTable:
        if not self.roguelike_topic_table_:
            self.roguelike_topic_table_ = RoguelikeTopicTable.convert(
                CacheData.readExcel('roguelike_topic_table')
            )
        return self.roguelike_topic_table_

    @property
    def SANDBOX_TABLE(self) -> SandboxTable:
        if not self.sandbox_table_:
            self.sandbox_table_ = SandboxTable.convert(
                CacheData.readExcel('sandbox_table')
            )
        return self.sandbox_table_

    @property
    def SHOP_CLIENT_TABLE(self) -> ShopClientTable:
        if not self.shop_client_table_:
            self.shop_client_table_ = ShopClientTable.convert(
                CacheData.readExcel('shop_client_table')
            )
        return self.shop_client_table_

    @property
    def SKILL_TABLE(self) -> Dict[str, SkillDataBundle]:
        if not self.skill_table_:
            self.skill_table_ = msgjson.decode(
                CacheData.readBytesExcel('skill_table'),
                type=Dict[str, SkillDataBundle]
            )
        return self.skill_table_

    @property
    def SKIN_TABLE(self) -> SkinTable:
        if not self.skin_table_:
            self.skin_table_ = SkinTable.convert(
                CacheData.readExcel('skin_table')
            )
        return self.skin_table_

    @property
    def STAGE_TABLE(self) -> StageTable:
        if not self.stage_table_:
            self.stage_table_ = StageTable.convert(
                CacheData.readExcel('stage_table')
            )
        return self.stage_table_

    @property
    def STORY_REVIEW_META_TABLE(self) -> StoryReviewMetaTable:
        if not self.story_review_meta_table_:
            self.story_review_meta_table_ = StoryReviewMetaTable.convert(
                CacheData.readExcel('story_review_meta_table')
            )
        return self.story_review_meta_table_

    @property
    def STORY_REVIEW_TABLE(self) -> Dict[str, StoryReviewGroupClientData]:
        if not self.story_review_table_:
            self.story_review_table_ = msgjson.decode(
                CacheData.readBytesExcel('story_review_table'),
                type=Dict[str, StoryReviewGroupClientData]
            )
        return self.story_review_table_

    @property
    def STORY_TABLE(self) -> Dict[str, StoryData]:
        if not self.story_table_:
            self.story_table_ = msgjson.decode(
                CacheData.readBytesExcel('story_table'),
                type=Dict[str, StoryData]
            )
        return self.story_table_

    @property
    def TECH_BUFF_TABLE(self) -> TechBuffTable:
        if not self.tech_buff_table_:
            self.tech_buff_table_ = TechBuffTable.convert(
                CacheData.readExcel('tech_buff_table')
            )
        return self.tech_buff_table_

    @property
    def TIP_TABLE(self) -> TipTable:
        if not self.tip_table_:
            self.tip_table_ = TipTable.convert(
                CacheData.readExcel('tip_table')
            )
        return self.tip_table_

    @property
    def TOKEN_TABLE(self) -> Dict[str, TokenCharacterData]:
        if not self.token_table_:
            self.token_table_ = msgjson.decode(
                CacheData.readBytesExcel('token_table'),
                type=Dict[str, TokenCharacterData]
            )
        return self.token_table_

    @property
    def UNIEQUIP_DATA(self) -> UniequipData:
        if not self.uniequip_data_:
            self.uniequip_data_ = UniequipData.convert(
                CacheData.readExcel('uniequip_data')
            )
        return self.uniequip_data_

    @property
    def UNIEQUIP_TABLE(self) -> UniEquipTable:
        if not self.uniequip_table_:
            self.uniequip_table_ = UniEquipTable.convert(
                CacheData.readExcel('uniequip_table')
            )
        return self.uniequip_table_

    @property
    def ZONE_TABLE(self) -> ZoneTable:
        if not self.zone_table_:
            self.zone_table_ = ZoneTable.convert(
                CacheData.readExcel('zone_table')
            )
        return self.zone_table_

    def preload_table(self) -> None:
        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if callable(method) and not name.startswith('__') \
                    and name != 'preload_table':
                method()


Excel = ExcelTableManager()
