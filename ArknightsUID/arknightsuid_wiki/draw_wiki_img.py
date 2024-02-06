import asyncio
import re
from pathlib import Path
from pprint import pformat
from typing import Dict, Union

from colorama import Fore, Style
from gsuid_core.utils.colortext.ColorText import ColorTextGroup, split_ctg
from gsuid_core.utils.image.image_tools import draw_text_by_line
from jinja2 import Template
from PIL import Image, ImageDraw

from ..arknightsuid_resource.constants import (
    BATTLE_EQUIP_TABLE,
    CHARACTER_TABLE,
    RANGE_TABLE,
    SKILL_TABLE,
    UNIEQUIP_TABLE,
    CharacterTable,
)
from ..utils.fonts.source_han_sans import (
    sans_font_18,
    sans_font_20,
    sans_font_24,
    sans_font_26,
    sans_font_34,
    sans_font_50,
    sans_font_120,
)

TEXTURE2D_PATH = Path(__file__).parent / 'texture2D'

bg_img = Image.open(TEXTURE2D_PATH / 'bg.jpg')
title_img = Image.open(TEXTURE2D_PATH / 'title.png')
vvan_img = Image.open(TEXTURE2D_PATH / 'char_4098_vvana_2b.png').resize((2000, 2000))

first_color = (29, 29, 29)
white_color = (255, 255, 255)
red_color = (235, 61, 75)
black_color = (0, 0, 0)

profession_en_to_cn = {
    'WARRIOR': '近卫',
    'SNIPER': '狙击',
    'TANK': '重装',
    'MEDIC': '医疗',
    'SUPPORT': '辅助',
    'CASTER': '术师',
    'SPECIAL': '特种',
    'PIONEER': '先锋',
    'TOKEN': '召唤物',
    'TRAP': '陷阱',
}

char_position_en_to_cn = {
    'MELEE': '近战',
    'RANGED': '远程',
    'ALL': '近战/远程',
    'NONE': '无',
}

attr_en_to_cn = {
    'maxHp': '生命',
    'atk': '攻击',
    'def_': '防御',
    'magicResistance': '法抗',
    'cost': '部署费用',
    'blockCnt': '阻挡',
    # "moveSpeed": "移动速度",
    'attackSpeed': '攻击速度',
    'baseAttackTime': '攻击间隔',
    'respawnTime': '再部署时间',
    # "hpRecoveryPerSec": "生命回复",
    # "spRecoveryPerSec": "技力回复",
    # "maxDeployCount": "部署数量上限",
    # "maxDeckStackCnt": "上场数量上限",
    # "tauntLevel": "嘲讽等级",
    # "massLevel": "重量",
    # "baseForceLevel": "推力等级",
    # "stunImmune": "眩晕免疫",
    # "silenceImmune": "沉默免疫",
    # "sleepImmune": "睡眠免疫",
    # "frozenImmune": "冰冻免疫",
    # "levitateImmune": "浮空免疫",
}

potential_id_to_cn = {
    0: '潜能2',
    1: '潜能3',
    2: '潜能4',
    3: '潜能5',
    4: '潜能6',
}


def test_ctg(length: int, *params):
    print(
        f'{Fore.GREEN}> running split_ctg(){Style.RESET_ALL}\
        \n    length: {length}\
        \n    texts: {params}'
    )
    groups_ = ColorTextGroup(list(params))
    f_ = pformat(split_ctg(groups_, length)).split('\n')
    print(Fore.CYAN, '\t', f_[0], '\n\t'.join(f_[0:]))


def render_template(template_str: str, data: Dict[str, Union[float, Union[int, None]]]):
    matches = re.finditer(r'\{([^}:]+)\}', template_str)
    matches_1 = re.finditer(r'\{([^{}]+):([^{}]+)\}', template_str)

    placeholder_data = {}
    for match in matches:
        placeholder = match.groups()
        formatting_option = ''
        placeholder_data[placeholder[0]] = (formatting_option, data.get(placeholder[0], ''))
    for match in matches_1:
        placeholder, formatting_option = match.groups()
        value = data.get(placeholder.replace('-', ''), '')
        # 可以在下列状态和初始状态间切换：\n攻击范围缩小，防御力+{def:0%}，
        # 每秒恢复最大生命的{HP_RECOVERY_PER_SEC_BY_MAX_HP_RATIO:0.0%}
        # {'def': 1, 'hp_recovery_per_sec_by_max_hp_ratio': 0.06}
        if value == '':
            value = data.get(placeholder.replace('-', '_').lower(), '')
        placeholder_data[placeholder] = (formatting_option, value)

    for placeholder, (formatting_option, value) in placeholder_data.items():
        if formatting_option == '':
            template_str = template_str.replace(f'{{{placeholder}}}', f'{value}')
        else:
            template_str = template_str.replace(
                f'{{{placeholder}:{formatting_option}}}', f'{value:{formatting_option}}'
            )

    template = Template(template_str)
    rendered_text = template.render()

    return rendered_text


async def get_equip_info(char_id: str):
    im = ''

    try:
        char_equip_id_list = UNIEQUIP_TABLE.charEquip[char_id]
    except KeyError:
        return '该干员没有模组'
    for char_equip_id in char_equip_id_list:
        equip_dict = UNIEQUIP_TABLE.equipDict[char_equip_id]
        uniequip_name = equip_dict.uniEquipName

        try:
            char_equip_phases = BATTLE_EQUIP_TABLE.equips[char_equip_id].phases
        except KeyError:
            continue

        im += f'模组名: {uniequip_name}\n'

        for equip_phase in char_equip_phases:
            equip_level = equip_phase.equipLevel
            im += '-----------------\n'
            im += f'等级: {equip_level}\n'
            equip_attribute_add_dict = {}
            equip_attribute_blackboard = equip_phase.attributeBlackboard
            for attribute in equip_attribute_blackboard:
                equip_attribute_add_dict[attribute.key] = attribute.value

            for attr in equip_attribute_add_dict:
                if attr in attr_en_to_cn:
                    im += f'{attr_en_to_cn[attr]}: +{equip_attribute_add_dict[attr]}\n'
            im += '-----------------\n'
            im += '效果:\n'
            for part in equip_phase.parts:
                target = part.target
                if target == 'TRAIT':
                    overrideTraitDataBundle = part.overrideTraitDataBundle
                    assert overrideTraitDataBundle.candidates is not None
                    for candidate in overrideTraitDataBundle.candidates:
                        additionalDescription = candidate.additionalDescription
                        blackboard = candidate.blackboard
                        blackboard_dict = {}
                        for blackboard_ in blackboard:
                            blackboard_dict[blackboard_.key] = blackboard_.value
                        if additionalDescription:
                            additionalDescription = re.sub(r'<[^>]+>', '', additionalDescription)
                            additionalDescription = render_template(additionalDescription, blackboard_dict)
                            additionalDescription = re.sub(r'.000000', '', additionalDescription)
                            im += f'{additionalDescription}\n'

                elif target == 'TALENT_DATA_ONLY':
                    addOrOverrideTalentDataBundle = part.addOrOverrideTalentDataBundle
                    assert addOrOverrideTalentDataBundle.candidates is not None
                    for candidate in addOrOverrideTalentDataBundle.candidates:
                        if candidate.requiredPotentialRank != 0:
                            continue
                        upgradeDescription = candidate.upgradeDescription
                        blackboard = candidate.blackboard
                        if upgradeDescription and blackboard:
                            upgradeDescription = re.sub(r'<[^>]+>', '', upgradeDescription)
                            im += f'{upgradeDescription}\n'

                elif target == 'DISPLAY':
                    overrideTraitDataBundle = part.overrideTraitDataBundle
                    assert overrideTraitDataBundle.candidates is not None
                    for candidate in overrideTraitDataBundle.candidates:
                        additionalDescription = candidate.additionalDescription
                        blackboard = candidate.blackboard
                        blackboard_dict = {}
                        for blackboard_ in blackboard:
                            blackboard_dict[blackboard_.key] = blackboard_.value
                        if additionalDescription and blackboard:
                            additionalDescription = re.sub(r'<[^>]+>', '', additionalDescription)
                            additionalDescription = render_template(additionalDescription, blackboard_dict)
                            additionalDescription = re.sub(r'.000000', '', additionalDescription)
                            im += f'{additionalDescription}\n'

                elif target == 'TALENT':
                    addOrOverrideTalentDataBundle = part.addOrOverrideTalentDataBundle
                    assert addOrOverrideTalentDataBundle.candidates is not None
                    for candidate in addOrOverrideTalentDataBundle.candidates:
                        upgradeDescription = candidate.upgradeDescription
                        if upgradeDescription == '':
                            continue
                        else:
                            upgradeDescription = re.sub(r'<[^>]+>', '', upgradeDescription)
                            im += f'{upgradeDescription}\n'

                elif target == 'TRAIT_DATA_ONLY':
                    overrideTraitDataBundle = part.overrideTraitDataBundle
                    assert overrideTraitDataBundle.candidates is not None
                    for candidate in overrideTraitDataBundle.candidates:
                        overrideDescripton = candidate.overrideDescripton
                        blackboard = candidate.blackboard
                        blackboard_dict = {}
                        for blackboard_ in blackboard:
                            blackboard_dict[blackboard_.key] = blackboard_.value
                        if overrideDescripton and blackboard:
                            overrideDescripton = re.sub(r'<[^>]+>', '', overrideDescripton)
                            overrideDescripton = render_template(overrideDescripton, blackboard_dict)
                            im += f'{overrideDescripton}\n'
                else:
                    raise NotImplementedError

        im += '-----------------\n'

    im = im[:-19]

    return im


async def get_wiki_info(char_id: str):
    im = ''

    character_data = CHARACTER_TABLE[char_id]

    char_name = character_data.name
    im += f'干员名: {char_name}\n'
    im += '-----------------\n'
    char_rarity = character_data.rarity
    im += f'星级: {str(char_rarity + 1)}\n'
    im += '-----------------\n'
    profession = character_data.profession
    im += f'职业: {profession_en_to_cn[profession]}\n'
    char_position = character_data.position
    im += f'攻击方式: {char_position_en_to_cn[char_position]}\n'
    sub_profession_id = character_data.subProfessionId
    sub_profession = UNIEQUIP_TABLE.subProfDict[sub_profession_id].subProfessionName
    im += f'子职业: {sub_profession}\n'
    im += '-----------------\n'
    nation_id = character_data.nationId
    group_id = character_data.groupId
    team_id = character_data.teamId

    im += '属性:\n'
    char_phases_data = character_data.phases[-1]
    char_max_phase = len(character_data.phases)
    char_max_level = char_phases_data.maxLevel
    char_attributes_key_frame = char_phases_data.attributesKeyFrames[-1].data
    for idx, attr in enumerate(char_attributes_key_frame):
        if attr[0] in attr_en_to_cn:
            im += f'{attr_en_to_cn[attr[0]]}: {attr[1]}\n'

    im += '-----------------\n'
    im += '天赋:\n'

    if character_data.talents:
        char_talent_num = len(character_data.talents)
        for talent in character_data.talents:
            if talent.candidates is None:
                continue
            talent_candidates = talent.candidates
            char_talent_name = talent_candidates[-1].name
            char_talent_description = talent_candidates[-1].description
            if char_talent_description:
                char_talent_description = re.sub(r'<[^>]+>', '', char_talent_description)
                im += f'{char_talent_name}: {char_talent_description}\n'

    char_potential_data = character_data.potentialRanks
    potential_add_dict: dict[int, tuple[int, float]] = {}
    im += '-----------------\n'
    im += '潜能加成\n'
    for potential_id, potential in enumerate(char_potential_data):
        potential_add_description = potential.description
        im += f'{potential_id_to_cn[potential_id]}: {potential_add_description}\n'
        if potential.buff:
            potential_add_attribute = potential.buff.attributes.attributeModifiers
            if len(potential.buff.attributes.attributeModifiers) == 1:
                potential_add_attribute_type = potential_add_attribute[0].attributeType
                potential_add_attribute_value = potential_add_attribute[0].value
                potential_add_dict[potential_id] = (
                    potential_add_attribute_type,
                    potential_add_attribute_value,
                )
            else:
                raise NotImplementedError
    im += '-----------------\n'

    if character_data.favorKeyFrames:
        char_favor_add_data = character_data.favorKeyFrames[-1].data
        im += '满信赖加成\n'
        for attr in char_favor_add_data:
            if attr[0] in ['maxHp', 'atk', 'def_', 'magicResistance'] and attr[1] != 0:
                im += f'{attr_en_to_cn[attr[0]]}: +{attr[1]}\n'

    im += '-----------------\n'
    skill_id_list: list[str] = []
    for skill in character_data.skills:
        if skill.skillId is None:
            continue
        skill_id_list.append(skill.skillId)

    im += '技能:\n'

    for skill in skill_id_list:
        skill_data = SKILL_TABLE.skills[skill]
        skill_level_data = skill_data.levels[-1]
        skill_name = skill_level_data.name
        im += f'技能名: {skill_name}\n'
        skill_type = skill_level_data.skillType
        skill_description = skill_level_data.description
        skill_sp_data = skill_level_data.spData
        skill_sp_type = skill_sp_data.spType

        if skill_sp_type == 1:
            im += '自动回复 '
        elif skill_sp_type == 2:
            im += '攻击回复 '
        elif skill_sp_type == 4:
            im += '受击回复 '
        elif skill_sp_type == 8:
            pass
        else:
            raise NotImplementedError

        if skill_type == 1:
            im += '手动触发\n'
        elif skill_type == 2:
            im += '自动触发\n'
        elif skill_type == 0:
            pass
        else:
            raise NotImplementedError

        skill_duration = skill_level_data.duration
        im += f'消耗: {skill_sp_data.spCost} '
        im += f'初始: {skill_sp_data.initSp} '
        im += f'持续: {str(skill_duration)}\n'
        skill_blackboard_data = skill_level_data.blackboard
        black_board_dict: dict[str, Union[Union[int, float], None]] = {}
        for black_board in skill_blackboard_data:
            black_board_dict[black_board.key] = black_board.value
        if skill_description:
            skill_description = skill_description.replace(':0.0', '')
            skill_description = re.sub(r'<[^>]+>', '', skill_description)
            skill_description = render_template(skill_description, black_board_dict).replace('--', '-')
            last_skill_description = re.sub(r'.000000', '', skill_description)
            if '{' in last_skill_description:
                raise NotImplementedError

            skill_desc = re.findall(r'[^\\n]+', last_skill_description)
            for skill_desc_line in skill_desc:
                im += f'{skill_desc_line}\n'
        im += '-----------------\n'
    im = im[:-19]

    return im


async def draw_wiki(char_id: str):
    img = Image.new('RGBA', (1500, 2800), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    img.paste(bg_img, (0, 0))
    img.paste(vvan_img, (-700, -100), vvan_img)
    img.paste(title_img, (0, -50), title_img)

    character_data = CHARACTER_TABLE[char_id]

    char_name = character_data.name
    draw.text(
        (144, 85),
        char_name,
        font=sans_font_120,
        fill=black_color,
        anchor='lm',
    )

    char_rarity = character_data.rarity
    rarity_img = Image.open(TEXTURE2D_PATH / f'rarity_yellow_{char_rarity}.png')
    img.paste(rarity_img, (960, 120), rarity_img)

    profession = character_data.profession
    profession_img = Image.open(TEXTURE2D_PATH / f'icon_{profession.lower()}.png')
    img.paste(profession_img, (1100, 7050), profession_img)

    bar_img = Image.open(TEXTURE2D_PATH / 'bar.png')
    light_line = Image.open(TEXTURE2D_PATH / 'light_line.png')
    bar_img.paste(light_line, (290, 60), light_line)
    bar_img_draw = ImageDraw.ImageDraw(bar_img)

    char_position = character_data.position
    char_position_cn = char_position_en_to_cn[char_position]
    bar_img_draw.text(
        (160, 100),
        char_position_cn,
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )

    sub_profession_id = character_data.subProfessionId
    sub_profession = UNIEQUIP_TABLE.subProfDict[sub_profession_id].subProfessionName
    bar_img_draw.text(
        (360, 100),
        sub_profession,
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )
    img.paste(bar_img, (40, 110), bar_img)

    nation_id = character_data.nationId
    bar_img = Image.open(TEXTURE2D_PATH / 'bar.png')
    light_line = Image.open(TEXTURE2D_PATH / 'light_line.png')
    bar_img.paste(light_line, (290, 60), light_line)
    bar_img_draw = ImageDraw.ImageDraw(bar_img)
    bar_img_draw.text(
        (155, 100),
        '势力',
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )
    bar_img_draw.text(
        (355, 100),
        nation_id if nation_id else '未知',
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )
    img.paste(bar_img, (940, 180 - 50), bar_img)

    group_id = character_data.groupId
    bar_img = Image.open(TEXTURE2D_PATH / 'bar.png')
    light_line = Image.open(TEXTURE2D_PATH / 'light_line.png')
    bar_img.paste(light_line, (290, 60), light_line)
    bar_img_draw = ImageDraw.ImageDraw(bar_img)
    bar_img_draw.text(
        (155, 100),
        '阵营',
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )
    bar_img_draw.text(
        (355, 100),
        group_id if group_id else '未知',
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )
    img.paste(bar_img, (940, 188 + 20), bar_img)

    team_id = character_data.teamId
    bar_img = Image.open(TEXTURE2D_PATH / 'bar.png')
    light_line = Image.open(TEXTURE2D_PATH / 'light_line.png')
    bar_img.paste(light_line, (290, 60), light_line)
    bar_img_draw = ImageDraw.ImageDraw(bar_img)
    bar_img_draw.text(
        (155, 100),
        '队伍',
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )
    bar_img_draw.text(
        (355, 100),
        team_id if team_id else '未知',
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )
    img.paste(bar_img, (940, 196 + 90), bar_img)

    char_phases_data = character_data.phases[-1]
    char_max_phase = len(character_data.phases)
    char_max_level = char_phases_data.maxLevel
    char_attributes_key_frame = char_phases_data.attributesKeyFrames[-1].data

    bar_img = Image.open(TEXTURE2D_PATH / 'bar.png')
    light_line = Image.open(TEXTURE2D_PATH / 'light_line.png')
    bar_img.paste(light_line, (320, 60), light_line)
    bar_img_draw = ImageDraw.ImageDraw(bar_img)
    bar_img_draw.text(
        (140, 100),
        '生命上限',
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )
    bar_img_draw.text(
        (420, 100),
        str(char_attributes_key_frame.maxHp),
        font=sans_font_34,
        fill=white_color,
        anchor='mm',
    )
    img.paste(bar_img, (940, 380), bar_img)

    bar_img = Image.open(TEXTURE2D_PATH / 'bar.png')
    light_line = Image.open(TEXTURE2D_PATH / 'light_line.png')
    bar_img.paste(light_line, (320, 60), light_line)
    bar_img_draw = ImageDraw.ImageDraw(bar_img)
    bar_img_draw.text(
        (140, 100),
        '攻击力',
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )
    bar_img_draw.text(
        (420, 100),
        str(char_attributes_key_frame.atk),
        font=sans_font_34,
        fill=white_color,
        anchor='mm',
    )
    img.paste(bar_img, (940, 380 + 78), bar_img)

    bar_img = Image.open(TEXTURE2D_PATH / 'bar.png')
    light_line = Image.open(TEXTURE2D_PATH / 'light_line.png')
    bar_img.paste(light_line, (320, 60), light_line)
    bar_img_draw = ImageDraw.ImageDraw(bar_img)
    bar_img_draw.text(
        (140, 100),
        '防御力',
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )
    bar_img_draw.text(
        (420, 100),
        str(char_attributes_key_frame.def_),
        font=sans_font_34,
        fill=white_color,
        anchor='mm',
    )
    img.paste(bar_img, (940, 380 + 78 * 2), bar_img)

    bar_img = Image.open(TEXTURE2D_PATH / 'bar.png')
    light_line = Image.open(TEXTURE2D_PATH / 'light_line.png')
    bar_img.paste(light_line, (320, 60), light_line)
    bar_img_draw = ImageDraw.ImageDraw(bar_img)
    bar_img_draw.text(
        (140, 100),
        '法抗',
        font=sans_font_34,
        fill=white_color,
        anchor='lm',
    )
    bar_img_draw.text(
        (420, 100),
        str(char_attributes_key_frame.magicResistance),
        font=sans_font_34,
        fill=white_color,
        anchor='mm',
    )
    img.paste(bar_img, (940, 380 + 78 * 3), bar_img)

    # 攻击范围
    range_id = char_phases_data.rangeId
    attack_area_img = Image.open(TEXTURE2D_PATH / 'attack_area.png')
    if range_id:
        range_data = RANGE_TABLE.range_[range_id]
        grids = range_data.grids
        area_0 = Image.open(TEXTURE2D_PATH / 'area_0.png').resize((58, 58))
        area_1 = Image.open(TEXTURE2D_PATH / 'area_1.png')
        for grid in grids:
            col = grid.col
            row = grid.row
            if col == 1 and row == 1:
                attack_area_img.paste(area_1, (90, 105), area_1)
            attack_area_img.paste(area_0, (105 + col * 56, 120 + row * 56), area_0)
    img.paste(attack_area_img, (915, 730), attack_area_img)

    char_potential_data = character_data.potentialRanks
    potential_add_dict: dict[int, tuple[int, float]] = {}
    for potential_id, potential in enumerate(char_potential_data):
        potential_add_description = potential.description
        if potential.buff:
            potential_add_attribute = potential.buff.attributes.attributeModifiers
            if len(potential.buff.attributes.attributeModifiers) == 1:
                potential_add_attribute_type = potential_add_attribute[0].attributeType
                potential_add_attribute_value = potential_add_attribute[0].value
                potential_add_dict[potential_id] = (
                    potential_add_attribute_type,
                    potential_add_attribute_value,
                )
            else:
                raise NotImplementedError

    if character_data.favorKeyFrames:
        char_favor_add_data = character_data.favorKeyFrames[-1].data

    talent_change_dict: dict[int, tuple[str, float]] = {}
    if character_data.talents:
        char_talent_num = len(character_data.talents)
        for talent in character_data.talents:
            if talent.candidates is None:
                continue
            talent_candidates = talent.candidates
            char_talent_name = talent_candidates[-1].name
            char_talent_description = talent_candidates[-1].description

    skill_id_list: list[str] = []
    for skill in character_data.skills:
        if skill.skillId is None:
            continue
        skill_id_list.append(skill.skillId)

    for skill in skill_id_list:
        skill_bg = Image.open(TEXTURE2D_PATH / 'skill_bg.png')
        skill3_bar_bg = Image.open(TEXTURE2D_PATH / 'skill3_bar.png')

        skill_data = SKILL_TABLE.skills[skill]
        skill_level_data = skill_data.levels[-1]
        skill_name = skill_level_data.name
        skill_description = skill_level_data.description
        skill_sp_data = skill_level_data.spData
        skill_duration = skill_level_data.duration
        skill_blackboard_data = skill_level_data.blackboard
        black_board_dict: dict[str, Union[Union[int, float], None]] = {}
        for black_board in skill_blackboard_data:
            black_board_dict[black_board.key] = black_board.value
        if skill_description:
            skill_description = re.sub(r'<[^>]+>', '', skill_description)
            skill_description = render_template(skill_description, black_board_dict).replace('--', '-')
            last_skill_description = re.sub(r'.000000', '', skill_description)
            print(last_skill_description)
            if '{' in last_skill_description:
                raise NotImplementedError
            # 匹配 -70% +200% 这种格式的数字
            c = re.sub(r'(\d+)%', r'\1%', last_skill_description)
            print(c)
            print(test_ctg(30, last_skill_description))
            draw_text_by_line(
                img=skill_bg,
                pos=(70, 20),
                text=last_skill_description,
                font=sans_font_24,
                fill='#3b4354',
                max_length=400,
            )
        # skill_bg.show()

    # img.show()

    return img


if __name__ == '__main__':
    asyncio.run(draw_wiki(char_id='char_4098_vvana'))
