from pydantic import BaseModel, Field


class Bank(BaseModel):
    name: str


class BGMBank(Bank):
    intro: str | None
    loop: str | None
    volume: float
    crossfade: float
    delay: float


class SoundFXBankSoundFX(BaseModel):
    asset: str
    weight: float
    important: bool
    is2D: bool
    delay: float
    minPitch: float
    maxPitch: float
    minVolume: float
    maxVolume: float
    ignoreTimeScale: bool


class SoundFXBank(Bank):
    sounds: list[SoundFXBankSoundFX] | None
    maxSoundAllowed: int
    popOldest: bool
    customMixerGroup: str | None
    loop: bool


class SoundFXCtrlBank(Bank):
    targetBank: str
    ctrlStop: bool
    ctrlStopFadetime: float
    name: str


class SnapshotBank(Bank):
    targetSnapshot: str
    hookSoundFxBank: str
    delay: float
    duration: float
    targetFxBank: Bank | None = None


class BattleVoiceOption(BaseModel):
    voiceType: int
    priority: int
    overlapIfSamePriority: bool
    cooldown: float
    delay: float


class MusicData(BaseModel):
    id_: str = Field(alias='id')
    name: str
    bank: str


class BattleVoiceData(BaseModel):
    crossfade: float
    minTimeDeltaForEnemyEncounter: float
    minSpCostForImportantPassiveSkill: int
    voiceTypeOptions: list[BattleVoiceOption]


class AudioData(BaseModel):
    __version__ = '23-07-27-18-50-06-aeb568'

    bgmBanks: list[BGMBank]
    soundFXBanks: list[SoundFXBank]
    soundFXCtrlBanks: list[SoundFXCtrlBank]
    snapshotBanks: list[SnapshotBank]
    battleVoice: BattleVoiceData
    musics: list[MusicData]
    soundFxVoiceLang: dict[str, dict[str, dict[str, str]]]
    bankAlias: dict[str, str]

    class Config:
        extra = 'allow'
