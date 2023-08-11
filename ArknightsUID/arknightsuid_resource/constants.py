import inspect

from ..utils.models.gamedata.ActivityTable import ActivityTable
from ..utils.models.gamedata.AudioData import AudioData
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
from ..utils.models.gamedata.DisplayMetaTable import DisplayMetaTable
from ..utils.models.gamedata.EnemyHandbookTable import EnemyHandbookTable
from ..utils.models.gamedata.FavorTable import FavorTable
from ..utils.models.gamedata.GachaTable import GachaTable
from ..utils.models.gamedata.GamedataConst import GamedataConst
from ..utils.models.gamedata.HandbookInfoTable import HandbookInfoTable
from ..utils.models.gamedata.HandbookTable import HandbookTable
from ..utils.models.gamedata.HandbookTeamTable import HandbookTeamTable
from ..utils.models.gamedata.ItemTable import ItemTable
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
from .cachedata import CacheData


class ExcelTableManager:
    activity_table_: ActivityTable | None = None
    audio_data_: AudioData | None = None
    battle_equip_table_: BattleEquipTable | None = None
    building_data_: BuildingData | None = None
    campaign_table_: CampaignTable | None = None
    chapter_table_: ChapterTable | None = None
    character_table_: CharacterTable | None = None
    char_meta_table_: CharMetaTable | None = None
    charm_table_: CharmTable | None = None
    char_patch_table_: CharPatchTable | None = None
    charword_table_: CharwordTable | None = None
    checkin_table_: CheckinTable | None = None
    climb_tower_table_: ClimbTowerTable | None = None
    clue_data_: ClueData | None = None
    crisis_table_: CrisisTable | None = None
    display_meta_table_: DisplayMetaTable | None = None
    enemy_handbook_table_: EnemyHandbookTable | None = None
    favor_table_: FavorTable | None = None
    gacha_table_: GachaTable | None = None
    gamedata_const_: GamedataConst | None = None
    handbook_info_table_: HandbookInfoTable | None = None
    handbook_table_: HandbookTable | None = None
    handbook_team_table_: HandbookTeamTable | None = None
    item_table_: ItemTable | None = None
    medal_table_: MedalTable | None = None
    mission_table_: MissionTable | None = None
    open_server_table_: OpenServerTable | None = None
    player_avatar_table_: PlayerAvatarTable | None = None
    range_table_: RangeTable | None = None
    replicate_table_: ReplicateTable | None = None
    retro_table_: RetroTable | None = None
    roguelike_table_: RoguelikeTable | None = None
    roguelike_topic_table_: RoguelikeTopicTable | None = None
    sandbox_table_: SandboxTable | None = None
    shop_client_table_: ShopClientTable | None = None
    skill_table_: SkillTable | None = None
    skin_table_: SkinTable | None = None
    stage_table_: StageTable | None = None
    story_review_meta_table_: StoryReviewMetaTable | None = None
    story_review_table_: StoryReviewTable | None = None
    story_table_: StoryTable | None = None
    tech_buff_table_: TechBuffTable | None = None
    tip_table_: TipTable | None = None
    token_table_: TokenTable | None = None
    uniequip_data_: UniequipData | None = None
    uniequip_table_: UniEquipTable | None = None
    zone_table_: ZoneTable | None = None

    @property
    def ACTIVITY_TABLE(self) -> ActivityTable:
        if not self.activity_table_:
            if hasattr(ActivityTable, 'model_validate'):
                self.activity_table_ = ActivityTable.model_validate(  # type: ignore
                    CacheData.readExcel('activity_table')
                )
            else:
                self.activity_table_ = ActivityTable.parse_obj(
                    CacheData.readExcel('activity_table')
                )
        return self.activity_table_

    @property
    def AUDIO_DATA(self) -> AudioData:
        if not self.audio_data_:
            if hasattr(AudioData, 'model_validate'):
                self.audio_data_ = AudioData.model_validate(  # type: ignore
                    CacheData.readExcel('audio_data')
                )
            else:
                self.audio_data_ = AudioData.parse_obj(
                    CacheData.readExcel('audio_data')
                )
        return self.audio_data_

    @property
    def BATTLE_EQUIP_TABLE(self) -> BattleEquipTable:
        if not self.battle_equip_table_:
            self.battle_equip_table_ = BattleEquipTable(
                CacheData.readExcel('battle_equip_table')
            )
        return self.battle_equip_table_

    @property
    def BUILDING_DATA(self) -> BuildingData:
        if not self.building_data_:
            if hasattr(BuildingData, 'model_validate'):
                self.building_data_ = BuildingData.model_validate(  # type: ignore
                    CacheData.readExcel('building_data')
                )
            else:
                self.building_data_ = BuildingData.parse_obj(
                    CacheData.readExcel('building_data')
                )
        return self.building_data_

    @property
    def CAMPAIGN_TABLE(self) -> CampaignTable:
        if not self.campaign_table_:
            if hasattr(CampaignTable, 'model_validate'):
                self.campaign_table_ = CampaignTable.model_validate(  # type: ignore
                    CacheData.readExcel('campaign_table')
                )
            else:
                self.campaign_table_ = CampaignTable.parse_obj(
                    CacheData.readExcel('campaign_table')
                )
        return self.campaign_table_

    @property
    def CHAPTER_TABLE(self) -> ChapterTable:
        if not self.chapter_table_:
            self.chapter_table_ = ChapterTable(CacheData.readExcel('chapter_table'))
        return self.chapter_table_

    @property
    def CHARATER_TABLE(self) -> CharacterTable:
        if not self.character_table_:
            if hasattr(CharacterTable, 'model_validate'):
                self.character_table_ = CharacterTable.model_validate(  # type: ignore
                    CacheData.readExcel('character_table')
                )
            else:
                self.character_table_ = CharacterTable(
                    CacheData.readExcel('character_table')
                )
        return self.character_table_

    @property
    def CHAR_META_TABLE(self) -> CharMetaTable:
        if not self.char_meta_table_:
            if hasattr(CharMetaTable, 'model_validate'):
                self.char_meta_table_ = CharMetaTable.model_validate(  # type: ignore
                    CacheData.readExcel('char_meta_table')
                )
            else:
                self.char_meta_table_ = CharMetaTable.parse_obj(
                    CacheData.readExcel('char_meta_table')
                )
        return self.char_meta_table_

    @property
    def CHARM_TABLE(self) -> CharmTable:
        if not self.charm_table_:
            if hasattr(CharmTable, 'model_validate'):
                self.charm_table_ = CharmTable.model_validate(  # type: ignore
                    CacheData.readExcel('charm_table')
                )
            else:
                self.charm_table_ = CharmTable.parse_obj(
                    CacheData.readExcel('charm_table')
                )
        return self.charm_table_

    @property
    def CHAR_PATH_TABLE(self) -> CharPatchTable:
        if not self.char_patch_table_:
            if hasattr(CharPatchTable, 'model_validate'):
                self.char_patch_table_ = CharPatchTable.model_validate(  # type: ignore
                    CacheData.readExcel('char_patch_table')
                )
            else:
                self.char_patch_table_ = CharPatchTable.parse_obj(
                    CacheData.readExcel('char_patch_table')
                )
        return self.char_patch_table_

    @property
    def CHARWORD_TABLE(self) -> CharwordTable:
        if not self.charword_table_:
            if hasattr(CharwordTable, 'model_validate'):
                self.charword_table_ = CharwordTable.model_validate(  # type: ignore
                    CacheData.readExcel('charword_table')
                )
            else:
                self.charword_table_ = CharwordTable.parse_obj(
                    CacheData.readExcel('charword_table')
                )
        return self.charword_table_

    @property
    def CHECKIN_TABLE(self) -> CheckinTable:
        if not self.checkin_table_:
            if hasattr(CheckinTable, 'model_validate'):
                self.checkin_table_ = CheckinTable.model_validate(  # type: ignore
                    CacheData.readExcel('checkin_table')
                )
            else:
                self.checkin_table_ = CheckinTable.parse_obj(
                    CacheData.readExcel('checkin_table')
                )
        return self.checkin_table_

    @property
    def CLIMB_TOWER_TABLE(self) -> ClimbTowerTable:
        if not self.climb_tower_table_:
            if hasattr(ClimbTowerTable, 'model_validate'):
                self.climb_tower_table_ = ClimbTowerTable.model_validate(  # type: ignore
                    CacheData.readExcel('climb_tower_table')
                )
            else:
                self.climb_tower_table_ = ClimbTowerTable.parse_obj(
                    CacheData.readExcel('climb_tower_table')
                )
        return self.climb_tower_table_

    @property
    def CLUE_DATA(self) -> ClueData:
        if not self.clue_data_:
            if hasattr(ClueData, 'model_validate'):
                self.clue_data_ = ClueData.model_validate(  # type: ignore
                    CacheData.readExcel('clue_data')
                )
            else:
                self.clue_data_ = ClueData.parse_obj(
                    CacheData.readExcel('clue_data')
                )
        return self.clue_data_

    @property
    def CRISIS_TABLE(self) -> CrisisTable:
        if not self.crisis_table_:
            if hasattr(CrisisTable, 'model_validate'):
                self.crisis_table_ = CrisisTable.model_validate(  # type: ignore
                    CacheData.readExcel('crisis_table')
                )
            else:
                self.crisis_table_ = CrisisTable.parse_obj(
                    CacheData.readExcel('crisis_table')
                )
        return self.crisis_table_

    @property
    def DISPLAY_META_TABLE(self) -> DisplayMetaTable:
        if not self.display_meta_table_:
            if hasattr(DisplayMetaTable, 'model_validate'):
                self.display_meta_table_ = DisplayMetaTable.model_validate(  # type: ignore
                    CacheData.readExcel('display_meta_table')
                )
            else:
                self.display_meta_table_ = DisplayMetaTable.parse_obj(
                    CacheData.readExcel('display_meta_table')
                )
        return self.display_meta_table_

    @property
    def ENEMY_HANDBOOK_TABLE(self) -> EnemyHandbookTable:
        if not self.enemy_handbook_table_:
            if hasattr(EnemyHandbookTable, 'model_validate'):
                self.enemy_handbook_table_ = EnemyHandbookTable.model_validate(  # type: ignore
                    CacheData.readExcel('enemy_handbook_table')
                )
            else:
                self.enemy_handbook_table_ = EnemyHandbookTable.parse_obj(
                    CacheData.readExcel('enemy_handbook_table')
                )
        return self.enemy_handbook_table_

    @property
    def FAVOR_TABLE(self) -> FavorTable:
        if not self.favor_table_:
            if hasattr(FavorTable, 'model_validate'):
                self.favor_table_ = FavorTable.model_validate(  # type: ignore
                    CacheData.readExcel('favor_table')
                )
            else:
                self.favor_table_ = FavorTable.parse_obj(
                    CacheData.readExcel('favor_table')
                )
        return self.favor_table_

    @property
    def GACHA_TABLE(self) -> GachaTable:
        if not self.gacha_table_:
            if hasattr(GachaTable, 'model_validate'):
                self.gacha_table_ = GachaTable.model_validate(  # type: ignore
                    CacheData.readExcel('gacha_table')
                )
            else:
                self.gacha_table_ = GachaTable.parse_obj(
                    CacheData.readExcel('gacha_table')
                )
        return self.gacha_table_

    @property
    def GAMEDATA_CONST(self) -> GamedataConst:
        if not self.gamedata_const_:
            if hasattr(GamedataConst, 'model_validate'):
                self.gamedata_const_ = GamedataConst.model_validate(  # type: ignore
                    CacheData.readExcel('gamedata_const')
                )
            else:
                self.gamedata_const_ = GamedataConst.parse_obj(
                    CacheData.readExcel('gamedata_const')
                )
        return self.gamedata_const_

    @property
    def HANDBOOK_INFO_TABLE(self) -> HandbookInfoTable:
        if not self.handbook_info_table_:
            if hasattr(HandbookInfoTable, 'model_validate'):
                self.handbook_info_table_ = HandbookInfoTable.model_validate(  # type: ignore
                    CacheData.readExcel('handbook_info_table')
                )
            else:
                self.handbook_info_table_ = HandbookInfoTable.parse_obj(
                    CacheData.readExcel('handbook_info_table')
                )
        return self.handbook_info_table_

    @property
    def HANDBOOK_TABLE(self) -> HandbookTable:
        if not self.handbook_table_:
            if hasattr(HandbookTable, 'model_validate'):
                self.handbook_table_ = HandbookTable.model_validate(  # type: ignore
                    CacheData.readExcel('handbook_table')
                )
            else:
                self.handbook_table_ = HandbookTable.parse_obj(
                    CacheData.readExcel('handbook_table')
                )
        return self.handbook_table_

    @property
    def HANDBOOK_TEAM_TABLE(self) -> HandbookTeamTable:
        if not self.handbook_team_table_:
            if hasattr(HandbookTeamTable, 'model_validate'):
                self.handbook_team_table_ = HandbookTeamTable.model_validate(  # type: ignore
                    CacheData.readExcel('handbook_team_table')
                )
            else:
                self.handbook_team_table_ = HandbookTeamTable.parse_obj(
                    CacheData.readExcel('handbook_team_table')
                )
        return self.handbook_team_table_

    @property
    def ITEM_TABLE(self) -> ItemTable:
        if not self.item_table_:
            if hasattr(ItemTable, 'model_validate'):
                self.item_table_ = ItemTable.model_validate(  # type: ignore
                    CacheData.readExcel('item_table')
                )
            else:
                self.item_table_ = ItemTable.parse_obj(
                    CacheData.readExcel('item_table')
                )
        return self.item_table_

    @property
    def MEDAL_TABLE(self) -> MedalTable:
        if not self.medal_table_:
            if hasattr(MedalTable, 'model_validate'):
                self.medal_table_ = MedalTable.model_validate(  # type: ignore
                    CacheData.readExcel('medal_table')
                )
            else:
                self.medal_table_ = MedalTable.parse_obj(
                    CacheData.readExcel('medal_table')
                )
        return self.medal_table_

    @property
    def MISSION_TABLE(self) -> MissionTable:
        if not self.mission_table_:
            if hasattr(MissionTable, 'model_validate'):
                self.mission_table_ = MissionTable.model_validate(  # type: ignore
                    CacheData.readExcel('mission_table')
                )
            else:
                self.mission_table_ = MissionTable.parse_obj(
                    CacheData.readExcel('mission_table')
                )
        return self.mission_table_

    @property
    def OPEN_SERVER_TABLE(self) -> OpenServerTable:
        if not self.open_server_table_:
            if hasattr(OpenServerTable, 'model_validate'):
                self.open_server_table_ = OpenServerTable.model_validate(  # type: ignore
                    CacheData.readExcel('open_server_table')
                )
            else:
                self.open_server_table_ = OpenServerTable.parse_obj(
                    CacheData.readExcel('open_server_table')
                )
        return self.open_server_table_

    @property
    def PLAYER_AVATAR_TABLE(self) -> PlayerAvatarTable:
        if not self.player_avatar_table_:
            if hasattr(PlayerAvatarTable, 'model_validate'):
                self.player_avatar_table_ = PlayerAvatarTable.model_validate(  # type: ignore
                    CacheData.readExcel('player_avatar_table')
                )
            else:
                self.player_avatar_table_ = PlayerAvatarTable.parse_obj(
                    CacheData.readExcel('player_avatar_table')
                )
        return self.player_avatar_table_

    @property
    def RANGE_TABLE(self) -> RangeTable:
        if not self.range_table_:
            if hasattr(RangeTable, 'model_validate'):
                self.range_table_ = RangeTable.model_validate(  # type: ignore
                    CacheData.readExcel('range_table')
                )
            else:
                self.range_table_ = RangeTable.parse_obj(
                    CacheData.readExcel('range_table')
                )
        return self.range_table_

    @property
    def REPLICATE_TABLE(self) -> ReplicateTable:
        if not self.replicate_table_:
            if hasattr(ReplicateTable, 'model_validate'):
                self.replicate_table_ = ReplicateTable.model_validate(  # type: ignore
                    CacheData.readExcel('replicate_table')
                )
            else:
                self.replicate_table_ = ReplicateTable.parse_obj(
                    CacheData.readExcel('replicate_table')
                )
        return self.replicate_table_

    @property
    def RETRO_TABLE(self) -> RetroTable:
        if not self.retro_table_:
            if hasattr(RetroTable, 'model_validate'):
                self.retro_table_ = RetroTable.model_validate(  # type: ignore
                    CacheData.readExcel('retro_table')
                )
            else:
                self.retro_table_ = RetroTable.parse_obj(
                    CacheData.readExcel('retro_table')
                )
        return self.retro_table_

    @property
    def ROGUELIKE_TABLE(self) -> RoguelikeTable:
        if not self.roguelike_table_:
            if hasattr(RoguelikeTable, 'model_validate'):
                self.roguelike_table_ = RoguelikeTable.model_validate(  # type: ignore
                    CacheData.readExcel('roguelike_table')
                )
            else:
                self.roguelike_table_ = RoguelikeTable.parse_obj(
                    CacheData.readExcel('roguelike_table')
                )
        return self.roguelike_table_

    @property
    def ROGUELIKE_TOPIC_TABLE(self) -> RoguelikeTopicTable:
        if not self.roguelike_topic_table_:
            if hasattr(RoguelikeTopicTable, 'model_validate'):
                self.roguelike_topic_table_ = RoguelikeTopicTable.model_validate(  # type: ignore
                    CacheData.readExcel('roguelike_topic_table')
                )
            else:
                self.roguelike_topic_table_ = RoguelikeTopicTable.parse_obj(
                    CacheData.readExcel('roguelike_topic_table')
                )
        return self.roguelike_topic_table_

    @property
    def SANDBOX_TABLE(self) -> SandboxTable:
        if not self.sandbox_table_:
            if hasattr(SandboxTable, 'model_validate'):
                self.sandbox_table_ = SandboxTable.model_validate(  # type: ignore
                    CacheData.readExcel('sandbox_table')
                )
            else:
                self.sandbox_table_ = SandboxTable.parse_obj(
                    CacheData.readExcel('sandbox_table')
                )
        return self.sandbox_table_

    @property
    def SHOP_CLIENT_TABLE(self) -> ShopClientTable:
        if not self.shop_client_table_:
            if hasattr(ShopClientTable, 'model_validate'):
                self.shop_client_table_ = ShopClientTable.model_validate(  # type: ignore
                    CacheData.readExcel('shop_client_table')
                )
            else:
                self.shop_client_table_ = ShopClientTable.parse_obj(
                    CacheData.readExcel('shop_client_table')
                )
        return self.shop_client_table_

    @property
    def SKILL_TABLE(self) -> SkillTable:
        if not self.skill_table_:
            self.skill_table_ = SkillTable(CacheData.readExcel('skill_table'))
        return self.skill_table_

    @property
    def SKIN_TABLE(self) -> SkinTable:
        if not self.skin_table_:
            if hasattr(SkinTable, 'model_validate'):
                self.skin_table_ = SkinTable.model_validate(  # type: ignore
                    CacheData.readExcel('skin_table')
                )
            else:
                self.skin_table_ = SkinTable.parse_obj(
                    CacheData.readExcel('skin_table')
                )
        return self.skin_table_

    @property
    def STAGE_TABLE(self) -> StageTable:
        if not self.stage_table_:
            if hasattr(StageTable, 'model_validate'):
                self.stage_table_ = StageTable.model_validate(  # type: ignore
                    CacheData.readExcel('stage_table')
                )
            else:
                self.stage_table_ = StageTable.parse_obj(
                    CacheData.readExcel('stage_table')
                )
        return self.stage_table_

    @property
    def STORY_REVIEW_META_TABLE(self) -> StoryReviewMetaTable:
        if not self.story_review_meta_table_:
            if hasattr(StoryReviewMetaTable, 'model_validate'):
                self.story_review_meta_table_ = StoryReviewMetaTable.model_validate(  # type: ignore
                    CacheData.readExcel('story_review_meta_table')
                )
            else:
                self.story_review_meta_table_ = StoryReviewMetaTable.parse_obj(
                    CacheData.readExcel('story_review_meta_table')
                )
        return self.story_review_meta_table_

    @property
    def STORY_REVIEW_TABLE(self) -> StoryReviewTable:
        if not self.story_review_table_:
            self.story_review_table_ = StoryReviewTable(
                CacheData.readExcel('story_review_table')
            )
        return self.story_review_table_

    @property
    def STORY_TABLE(self) -> StoryTable:
        if not self.story_table_:
            self.story_table_ = StoryTable(CacheData.readExcel('story_table'))
        return self.story_table_

    @property
    def TECH_BUFF_TABLE(self) -> TechBuffTable:
        if not self.tech_buff_table_:
            if hasattr(TechBuffTable, 'model_validate'):
                self.tech_buff_table_ = TechBuffTable.model_validate(  # type: ignore
                    CacheData.readExcel('tech_buff_table')
                )
            else:
                self.tech_buff_table_ = TechBuffTable.parse_obj(
                    CacheData.readExcel('tech_buff_table')
                )
        return self.tech_buff_table_

    @property
    def TIP_TABLE(self) -> TipTable:
        if not self.tip_table_:
            if hasattr(TipTable, 'model_validate'):
                self.tip_table_ = TipTable.model_validate(  # type: ignore
                    CacheData.readExcel('tip_table')
                )
            else:
                self.tip_table_ = TipTable.parse_obj(
                    CacheData.readExcel('tip_table')
                )
        return self.tip_table_

    @property
    def TOKEN_TABLE(self) -> TokenTable:
        if not self.token_table_:
            self.token_table_ = TokenTable(CacheData.readExcel('token_table'))
        return self.token_table_

    @property
    def UNIEQUIP_DATA(self) -> UniequipData:
        if not self.uniequip_data_:
            if hasattr(UniequipData, 'model_validate'):
                self.uniequip_data_ = UniequipData.model_validate(  # type: ignore
                    CacheData.readExcel('uniequip_data')
                )
            else:
                self.uniequip_data_ = UniequipData.parse_obj(
                    CacheData.readExcel('uniequip_data')
                )
        return self.uniequip_data_

    @property
    def UNIEQUIP_TABLE(self) -> UniEquipTable:
        if not self.uniequip_table_:
            if hasattr(UniEquipTable, 'model_validate'):
                self.uniequip_table_ = UniEquipTable.model_validate(  # type: ignore
                    CacheData.readExcel('uniequip_table')
                )
            else:
                self.uniequip_table_ = UniEquipTable.parse_obj(
                    CacheData.readExcel('uniequip_table')
                )
        return self.uniequip_table_

    @property
    def ZONE_TABLE(self) -> ZoneTable:
        if not self.zone_table_:
            if hasattr(ZoneTable, 'model_validate'):
                self.zone_table_ = ZoneTable.model_validate(  # type: ignore
                    CacheData.readExcel('zone_table')
                )
            else:
                self.zone_table_ = ZoneTable.parse_obj(
                    CacheData.readExcel('zone_table')
                )
        return self.zone_table_

    def preload_table(self) -> None:
        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if callable(method) and not name.startswith('__') \
                    and name != 'preload_table':
                method()


Excel = ExcelTableManager()
