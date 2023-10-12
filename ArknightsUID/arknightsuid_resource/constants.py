import asyncio
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
from .memoryStore import store


class ExcelTableManager:
    activity_table_: ActivityTable
    audio_data_: AudioData
    battle_equip_table_: BattleEquipTable
    building_data_: BuildingData
    campaign_table_: CampaignTable
    chapter_table_: ChapterTable
    character_table_: CharacterTable
    char_meta_table_: CharMetaTable
    charm_table_: CharmTable
    char_patch_table_: CharPatchTable
    charword_table_: CharwordTable
    checkin_table_: CheckinTable
    climb_tower_table_: ClimbTowerTable
    clue_data_: ClueData
    crisis_table_: CrisisTable
    display_meta_table_: DisplayMetaTable
    enemy_handbook_table_: EnemyHandbookTable
    favor_table_: FavorTable
    gacha_table_: GachaTable
    gamedata_const_: GamedataConst
    handbook_info_table_: HandbookInfoTable
    handbook_table_: HandbookTable
    handbook_team_table_: HandbookTeamTable
    item_table_: ItemTable
    medal_table_: MedalTable
    mission_table_: MissionTable
    open_server_table_: OpenServerTable
    player_avatar_table_: PlayerAvatarTable
    range_table_: RangeTable
    replicate_table_: ReplicateTable
    retro_table_: RetroTable
    roguelike_table_: RoguelikeTable
    roguelike_topic_table_: RoguelikeTopicTable
    sandbox_table_: SandboxTable
    shop_client_table_: ShopClientTable
    skill_table_: SkillTable
    skin_table_: SkinTable
    stage_table_: StageTable
    story_review_meta_table_: StoryReviewMetaTable
    story_review_table_: StoryReviewTable
    story_table_: StoryTable
    tech_buff_table_: TechBuffTable
    tip_table_: TipTable
    token_table_: TokenTable
    uniequip_data_: UniequipData
    uniequip_table_: UniEquipTable
    zone_table_: ZoneTable

    async def activity_table(self) -> None:
        self.activity_table_ = ActivityTable.convert(
            await store.get_excel("activity_table")
        )

    @property
    def ACTIVITY_TABLE(self) -> ActivityTable:
        return self.activity_table_

    async def audio_data(self) -> None:
        self.audio_data_ = AudioData.convert(
            await store.get_excel("audio_data")
        )

    @property
    def AUDIO_DATA(self) -> AudioData:
        return self.audio_data_

    async def battle_equip_table(self) -> None:
        self.battle_equip_table_ = BattleEquipTable.convert(
            {"equips": await store.get_excel("battle_equip_table")}
        )

    @property
    def BATTLE_EQUIP_TABLE(self) -> BattleEquipTable:
        return self.battle_equip_table_

    async def building_data(self) -> None:
        self.building_data_ = BuildingData.convert(
            await store.get_excel("building_data")
        )

    @property
    def BUILDING_DATA(self) -> BuildingData:
        return self.building_data_

    async def campaign_table(self) -> None:
        self.campaign_table_ = CampaignTable.convert(
            await store.get_excel("campaign_table")
        )

    @property
    def CAMPAIGN_TABLE(self) -> CampaignTable:
        return self.campaign_table_

    async def chapter_table(self) -> None:
        self.chapter_table_ = ChapterTable.convert(
            {"chapters": await store.get_excel("chapter_table")}
        )

    @property
    def CHAPTER_TABLE(self) -> ChapterTable:
        return self.chapter_table_

    async def character_table(self) -> None:
        self.character_table_ = CharacterTable.convert(
            {"chars": await store.get_excel("character_table")}
        )

    @property
    def CHARATER_TABLE(self) -> CharacterTable:
        return self.character_table_

    async def char_meta_table(self) -> None:
        self.char_meta_table_ = CharMetaTable.convert(
            await store.get_excel("char_meta_table")
        )

    @property
    def CHAR_META_TABLE(self) -> CharMetaTable:
        return self.char_meta_table_

    async def charm_table(self) -> None:
        self.charm_table_ = CharmTable.convert(
            await store.get_excel("charm_table")
        )

    @property
    def CHARM_TABLE(self) -> CharmTable:
        return self.charm_table_

    async def char_patch_table(self) -> None:
        self.char_patch_table_ = CharPatchTable.convert(
            await store.get_excel("char_patch_table")
        )

    @property
    def CHAR_PATH_TABLE(self) -> CharPatchTable:
        return self.char_patch_table_

    async def charword_table(self) -> None:
        self.charword_table_ = CharwordTable.convert(
            await store.get_excel("charword_table")
        )

    @property
    def CHARWORD_TABLE(self) -> CharwordTable:
        return self.charword_table_

    async def checkin_table(self) -> None:
        self.checkin_table_ = CheckinTable.convert(
            await store.get_excel("checkin_table")
        )

    @property
    def CHECKIN_TABLE(self) -> CheckinTable:
        return self.checkin_table_

    async def climb_tower_table(self) -> None:
        self.climb_tower_table_ = ClimbTowerTable.convert(
            await store.get_excel("climb_tower_table")
        )

    @property
    def CLIMB_TOWER_TABLE(self) -> ClimbTowerTable:
        return self.climb_tower_table_

    async def clue_data(self) -> None:
        self.clue_data_ = ClueData.convert(await store.get_excel("clue_data"))

    @property
    def CLUE_DATA(self) -> ClueData:
        return self.clue_data_

    async def crisis_table(self) -> None:
        self.crisis_table_ = CrisisTable.convert(
            await store.get_excel("crisis_table")
        )

    @property
    def CRISIS_TABLE(self) -> CrisisTable:
        return self.crisis_table_

    async def display_meta_table(self) -> None:
        self.display_meta_table_ = DisplayMetaTable.convert(
            await store.get_excel("display_meta_table")
        )

    @property
    def DISPLAY_META_TABLE(self) -> DisplayMetaTable:
        return self.display_meta_table_

    async def enemy_handbook_table(self) -> None:
        self.enemy_handbook_table_ = EnemyHandbookTable.convert(
            await store.get_excel("enemy_handbook_table")
        )

    @property
    def ENEMY_HANDBOOK_TABLE(self) -> EnemyHandbookTable:
        return self.enemy_handbook_table_

    async def favor_table(self) -> None:
        self.favor_table_ = FavorTable.convert(
            await store.get_excel("favor_table")
        )

    @property
    def FAVOR_TABLE(self) -> FavorTable:
        return self.favor_table_

    async def gacha_table(self) -> None:
        self.gacha_table_ = GachaTable.convert(
            await store.get_excel("gacha_table")
        )

    @property
    def GACHA_TABLE(self) -> GachaTable:
        return self.gacha_table_

    async def gamedata_const(self) -> None:
        self.gamedata_const_ = GamedataConst.convert(
            await store.get_excel("gamedata_const")
        )

    @property
    def GAMEDATA_CONST(self) -> GamedataConst:
        return self.gamedata_const_

    async def handbook_info_table(self) -> None:
        self.handbook_info_table_ = HandbookInfoTable.convert(
            await store.get_excel("handbook_info_table")
        )

    @property
    def HANDBOOK_INFO_TABLE(self) -> HandbookInfoTable:
        return self.handbook_info_table_

    async def handbook_table(self) -> None:
        self.handbook_table_ = HandbookTable.convert(
            await store.get_excel("handbook_table")
        )

    @property
    def HANDBOOK_TABLE(self) -> HandbookTable:
        return self.handbook_table_

    async def handbook_team_table(self) -> None:
        self.handbook_team_table_ = HandbookTeamTable.convert(
            {"team": await store.get_excel("handbook_team_table")}
        )

    @property
    def HANDBOOK_TEAM_TABLE(self) -> HandbookTeamTable:
        return self.handbook_team_table_

    async def item_table(self) -> None:
        self.item_table_ = ItemTable.convert(
            await store.get_excel("item_table")
        )

    @property
    def ITEM_TABLE(self) -> ItemTable:
        return self.item_table_

    async def medal_table(self) -> None:
        self.medal_table_ = MedalTable.convert(
            await store.get_excel("medal_table")
        )

    @property
    def MEDAL_TABLE(self) -> MedalTable:
        return self.medal_table_

    async def mission_table(self) -> None:
        self.mission_table_ = MissionTable.convert(
            await store.get_excel("mission_table")
        )

    @property
    def MISSION_TABLE(self) -> MissionTable:
        return self.mission_table_

    async def open_server_table(self) -> None:
        self.open_server_table_ = OpenServerTable.convert(
            await store.get_excel("open_server_table")
        )

    @property
    def OPEN_SERVER_TABLE(self) -> OpenServerTable:
        return self.open_server_table_

    async def player_avatar_table(self) -> None:
        self.player_avatar_table_ = PlayerAvatarTable.convert(
            await store.get_excel("player_avatar_table")
        )

    @property
    def PLAYER_AVATAR_TABLE(self) -> PlayerAvatarTable:
        return self.player_avatar_table_

    async def range_table(self) -> None:
        self.range_table_ = RangeTable.convert(
            {"range_": await store.get_excel("range_table")}
        )

    @property
    def RANGE_TABLE(self) -> RangeTable:
        return self.range_table_

    async def replicate_table(self) -> None:
        self.replicate_table_ = ReplicateTable.convert(
            {"replicate": await store.get_excel("replicate_table")}
        )

    @property
    def REPLICATE_TABLE(self) -> ReplicateTable:
        return self.replicate_table_

    async def retro_table(self) -> None:
        self.retro_table_ = RetroTable.convert(
            await store.get_excel("retro_table")
        )

    @property
    def RETRO_TABLE(self) -> RetroTable:
        return self.retro_table_

    async def roguelike_table(self) -> None:
        self.roguelike_table_ = RoguelikeTable.convert(
            await store.get_excel("roguelike_table")
        )

    @property
    def ROGUELIKE_TABLE(self) -> RoguelikeTable:
        return self.roguelike_table_

    async def roguelike_topic_table(self) -> None:
        self.roguelike_topic_table_ = RoguelikeTopicTable.convert(
            await store.get_excel("roguelike_topic_table")
        )

    @property
    def ROGUELIKE_TOPIC_TABLE(self) -> RoguelikeTopicTable:
        return self.roguelike_topic_table_

    async def sandbox_table(self) -> None:
        self.sandbox_table_ = SandboxTable.convert(
            await store.get_excel("sandbox_table")
        )

    @property
    def SANDBOX_TABLE(self) -> SandboxTable:
        return self.sandbox_table_

    async def shop_client_table(self) -> None:
        self.shop_client_table_ = ShopClientTable.convert(
            await store.get_excel("shop_client_table")
        )

    @property
    def SHOP_CLIENT_TABLE(self) -> ShopClientTable:
        return self.shop_client_table_

    async def skill_table(self) -> None:
        self.skill_table_ = SkillTable.convert(
            {"skills": await store.get_excel("skill_table")}
        )

    @property
    def SKILL_TABLE(self) -> SkillTable:
        return self.skill_table_

    async def skin_table(self) -> None:
        self.skin_table_ = SkinTable.convert(
            await store.get_excel("skin_table")
        )

    @property
    def SKIN_TABLE(self) -> SkinTable:
        return self.skin_table_

    async def stage_table(self) -> None:
        self.stage_table_ = StageTable.convert(
            await store.get_excel("stage_table")
        )

    @property
    def STAGE_TABLE(self) -> StageTable:
        return self.stage_table_

    async def story_review_meta_table(self) -> None:
        self.story_review_meta_table_ = StoryReviewMetaTable.convert(
            await store.get_excel("story_review_meta_table")
        )

    @property
    def STORY_REVIEW_META_TABLE(self) -> StoryReviewMetaTable:
        return self.story_review_meta_table_

    async def story_review_table(self) -> None:
        self.story_review_table_ = StoryReviewTable.convert(
            {"storyreviewtable": await store.get_excel("story_review_table")}
        )

    @property
    def STORY_REVIEW_TABLE(self) -> StoryReviewTable:
        return self.story_review_table_

    async def story_table(self) -> None:
        self.story_table_ = StoryTable.convert(
            {"stories": await store.get_excel("story_table")}
        )

    @property
    def STORY_TABLE(self) -> StoryTable:
        return self.story_table_

    async def tech_buff_table(self) -> None:
        self.tech_buff_table_ = TechBuffTable.convert(
            await store.get_excel("tech_buff_table")
        )

    @property
    def TECH_BUFF_TABLE(self) -> TechBuffTable:
        return self.tech_buff_table_

    async def tip_table(self) -> None:
        self.tip_table_ = TipTable.convert(await store.get_excel("tip_table"))

    @property
    def TIP_TABLE(self) -> TipTable:
        return self.tip_table_

    async def token_table(self) -> None:
        self.token_table_ = TokenTable.convert(
            {"tokens": await store.get_excel("token_table")}
        )

    @property
    def TOKEN_TABLE(self) -> TokenTable:
        return self.token_table_

    async def uniequip_data(self) -> None:
        self.uniequip_data_ = UniequipData.convert(
            await store.get_excel("uniequip_data")
        )

    @property
    def UNIEQUIP_DATA(self) -> UniequipData:
        return self.uniequip_data_

    async def uniequip_table(self) -> None:
        self.uniequip_table_ = UniEquipTable.convert(
            await store.get_excel("uniequip_table")
        )

    @property
    def UNIEQUIP_TABLE(self) -> UniEquipTable:
        return self.uniequip_table_

    async def zone_table(self) -> None:
        self.zone_table_ = ZoneTable.convert(
            await store.get_excel("zone_table")
        )

    @property
    def ZONE_TABLE(self) -> ZoneTable:
        return self.zone_table_

    async def preload_table(self) -> None:
        tasks = []
        for name, method in inspect.getmembers(self):
            if (
                inspect.iscoroutinefunction(method)
                and not name.startswith("__")
                and name != "preload_table"
            ):
                await method()
        await asyncio.gather(*tasks)


Excel = ExcelTableManager()
