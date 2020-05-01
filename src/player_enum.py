"""
"""

from enum import IntEnum

class ClassID(IntEnum):
    KNIGHT = 128
    MAGE = 129
    ARCHER = 130
    THIEF = 131


class SkillUSE():
    def __init__(self):
        self.ATTACK = False
        # Knight
        self.LIGHTENING_SLASH = False
        self.TRANSCENDENTAL_BLOW  = False
        self.FLASHING_SLASH = False
        
        self.MOCKERY = False
        self.UPWARD_SLASH = False
        self.PROVOCATION = False
        self.INCREASING_CONCENTRATION = False
        self.WIDENING_WOUND = False
        self.PROTECT = False
        self.SHIELD_ATTACK = False
        self.POWERFUL_UPWARD_SLASH = False
        self.BRUTAL_ATTACK = False
        self.FORCE_OF_DEFENSE = False
        self.CALL_OF_DEFENSE = False
        self.RUSH = False
        self.SHIELD_OFFENSE = False
        self.CALL_OF_RECOVERY = False
        self.BERSERK = False
        self.HALF_SWING = False
        self.SACRIFICE = False
        self.CALL_OF_LIGHTNING_DEFENSE = False
        self.CALL_OF_ICE_DEFENSE = False
        self.CALL_OF_FIRE_DEFENSE = False
        self.CALL_OF_ON_TARGET_POINT = False
        self.CALL_OF_PHYSICAL_ATTACK = False
        self.SURVIVAL_INSTINCT = False
        self.ELASTIC_SHIELD = False
        self.REVIVAL = False
        self.PERFECT_DEFENSE = False
        self.SPIN_SLASH = False
        self.POWERFUL_WIDENING_WOUND = False
        self.WALK_ON_AIR = False
        self.SHOUT_OF_DEFENSE = False
        self.THE_BOOM_OF_EARTH = False
        self.SHOUT_OF_FIGHTING_SPIRIT = False
        self.THE_WAVE_OF_EARTH = False
        # MAGES
        self.BUFF_MEDITATION = False
        self.BUFF_DEF_INCANTATION = False
        self.BUFF_DEF = False
        self.BUFF_HP = False
        self.BUFF_AGI = False
        self.BUFF_INT = False
        self.BUFF_CRIT = False
        self.BUFF_STR = False
        self.GROUP_CURE = False
        self.GROUP_CURE_2 = False        
        self.CURE_2 = False
        self.CURE_3 = False
        self.REFINING_WEAPON = False
        self.LIGHT_MAGIC = False
        self.FIRE_MAGIC = False
        self.ICE_MAGIC = False
        self.LIGHTENING_BLOW = False
        self.LIGHT_SUMMON = False
        self.SHOCK_WAVE = False
        self.FLAME_BOMB = False
        self.THUNDER = False
        self.EXPLOSION = False
        self.SPLASHY_ICE = False
        self.FIRE_BLOW = False
        self.ICE_RESTRICTION = False
        self.CHAIN_LIGHTENING = False
        self.EXPLOSIVE_BURST = False
        self.BLESSING = False
        # ARCHER
        self.STAGGERING_BLOW = False
        self.FLAMY_ARROW = False
        self.CHANCE_CAPTURE = False
        self.MUSCLE_SOLIDATION = False
        self.BLOW_UP_ARROW = False
        self.POISON_ARROW = False
        self.MYSTERIOUS_ARROW = False
        self.NON_ATRI_ERSIST = False
        self.HEARTH_BREAKER = False
        self.LIFE_ABSORPTION = False
        self.PAIN = False
        # THIEF
        self.DOK = False
        self.SPIN_ATTACK = False
        self.CONFUSION = False
        self.ARMOR_BREAKER = False
        self.TWINBLADE_STRIKE = False
        self.COUNTER_ATTACK = False


class SkillID(IntEnum):
        # SKILL IDs
    BETHEAD = 0x01
    LIFE_EXTENSION = 0x1e
        # Knight
    LIGHTENING_SLASH = 0x03
    TRANSCENDENTAL_BLOW = 0x05
    FLASHING_SLASH = 0x09

    MOCKERY = 0x04
    UPWARD_SLASH = 0x07
    PROVOCATION = 0x08
    INCREASING_CONCENTRATION = 0x0a
    WIDENING_WOUND = 0x0d
    PROTECT = 0x0e
    SHIELD_ATTACK = 0x0f
    POWERFUL_UPWARD_SLASH = 0x10
    BRUTAL_ATTACK = 17
    FORCE_OF_DEFENSE = 18
    CALL_OF_DEFENSE = 19
    RUSH = 21
    SHIELD_OFFENSE = 22
    CALL_OF_RECOVERY = 23
    BERSERK = 24
    HALF_SWING = 25
    SACRIFICE = 26
    CALL_OF_LIGHTNING_DEFENSE = 27
    CALL_OF_ICE_DEFENSE = 28
    CALL_OF_FIRE_DEFENSE = 29
    CALL_OF_ON_TARGET_POINT = 31
    CALL_OF_PHYSICAL_ATTACK = 32
    SURVIVAL_INSTINCT = 33
    ELASTIC_SHIELD = 34
    REVIVAL = 35
    PERFECT_DEFENSE = 40
    SPIN_SLASH = 38
    POWERFUL_WIDENING_WOUND = 41
    WALK_ON_AIR = 95
    SHOUT_OF_DEFENSE = 90
    THE_BOOM_OF_EARTH = 91
    SHOUT_OF_FIGHTING_SPIRIT = 92
    THE_WAVE_OF_EARTH = 93
        # MAGES
    BUFF_MEDITATION = 0x0F
    BUFF_DEF_INCANTATION = 0x15
    GROUP_CURE = 0x1C
    GROUP_CURE_2 = 0x39
    BUFF_DEF = 0x27
    BUFF_HP = 0x32
    BUFF_AGI = 0x33
    BUFF_INT = 0x34
    BUFF_CRIT = 0x35
    BUFF_STR = 0x31
    CURE_2 = 0x16
    CURE_3 = 0x23
    REFINING_WEAPON = 0x26
    LIGHT_MAGIC = 0x04
    FIRE_MAGIC = 0x02
    ICE_MAGIC = 0x03
    LIGHTENING_BLOW = 0x17
    LIGHTENING_SUMMONS = 0x1F
    SHOCK_WAVE = 0x09
    FLAME_BOMB = 0x21
    THUNDER = 0x2A
    EXPLOSION = 0x2E
    SPLASHY_ICE = 0x18
    FIRE_BLOW = 0x19
    ICE_RESTRICTION = 0x2C
    CHAIN_LIGHTENING = 0x29
    EXPLOSIVE_BURST = 0x2F
    SOULDESTRUCTION = 0x28
    BLESSING = 0x45
        # ARCHER
    STAGGERING_BLOW = 0x03 # ok
    FLAMY_ARROW = 0x06
    CHANCE_CAPTURE = 0x07
    MUSCLE_SOLIDATION = 0x0A
    BLOW_UP_ARROW = 0x0E
    POISON_ARROW = 0x0D
    MYSTERIOUS_ARROW = 0x15
    NON_ATRI_ERSIST = 0x1D
    HEARTH_BREAKER = 0x09 # ok
    LIFE_ABSORPTION = 0x12
    PAIN = 0x13
        # THIEF
    DOK = 0x0d  # B=skillid
    SPIN_ATTACK = 0x13 # spinattack=BBL
    CONFUSION = 0x09
    ARMOR_BREAKER = 0x16
    TWINBLADE_STRIKE = 0x17
    COUNTER_ATTACK = 0x14 # b       
        


class SkillTIME():
    def __init__(self):
        """Time when skill is ready again
        """
        self.ATTACK = 0
        self.CONSUME_ITEM = 0
            # KNIGHT
        self.LIGHTENING_SLASH = 0
        self.TRANSCENDENTAL_BLOW = 0
        self.FLASHING_SLASH = 0
        self.MOCKERY = 0
        self.UPWARD_SLASH = 0
        self.PROVOCATION = 0
        self.INCREASING_CONCENTRATION = 0
        self.WIDENING_WOUND = 0
        self.PROTECT = 0
        self.SHIELD_ATTACK = 0
        self.POWERFUL_UPWARD_SLASH = 0
        self.BRUTAL_ATTACK = 0
        self.FORCE_OF_DEFENSE = 0
        self.CALL_OF_DEFENSE = 0
        self.RUSH = 0
        self.SHIELD_OFFENSE = 0
        self.CALL_OF_RECOVERY = 0
        self.BERSERK = 0
        self.HALF_SWING = 0
        self.SACRIFICE = 0
        self.CALL_OF_LIGHTNING_DEFENSE = 0
        self.CALL_OF_ICE_DEFENSE = 0
        self.CALL_OF_FIRE_DEFENSE = 0
        self.CALL_OF_ON_TARGET_POINT = 0
        self.CALL_OF_PHYSICAL_ATTACK = 0
        self.SURVIVAL_INSTINCT = 0
        self.ELASTIC_SHIELD = 0
        self.REVIVAL = 0
        self.PERFECT_DEFENSE = 0
        self.SPIN_SLASH = 0
        self.POWERFUL_WIDENING_WOUND = 0
        self.WALK_ON_AIR = 0
        self.SHOUT_OF_DEFENSE = 0
        self.THE_BOOM_OF_EARTH = 0
        self.SHOUT_OF_FIGHTING_SPIRIT = 0
        self.THE_WAVE_OF_EARTH = 0        
            # MAGE
        self.BUFF_DEF_INCANTATION = 0
        self.BUFF_MEDITATION = 0
        self.LIGHT_MAGIC = 0
        self.ICE_MAGIC = 0
        self.FIRE_MAGIC = 0  # less if fire mastery learned
        self.LIGHTENING_BLOW = 0
        self.SHOCK_WAVE = 0
        self.SPLASHY_ICE = 0
        self.FIRE_BLOW = 0
        self.SPEED_UP = 0
        self.GROUP_CURE = 0
        self.LIGHTENING_SUMMONS = 0
        self.HAIL = 0
        self.FLAME_BOMB = 0
        self.CURE_3 = 0
        self.REFINING_WEAPON = 0        
        self.SOULDESTRUCTION = 0
        self.CHAIN_LIGHTENING = 0
        self.THUNDER = 0
        self.THUNDER_STORM = 0
        self.ICE_RESTRICTION = 0
        self.ICE_STORM = 0
        self.EXPLOSION = 0
        self.EXPLOSIVE_BURST = 0
        self.FIRE_STORM = 0
        self.BUFF_DEF = 0
        self.BUFF_STR = 0
        self.BUFF_HP = 0
        self.BUFF_AGI = 0
        self.BUFF_INT = 0
        self.BUFF_CRIT = 0
        self.PERFECT_CURE = 0
        self.GROUP_CURE_2 = 0
        self.PERFECT_GROUP_CURE_2 = 0
        self.PERFECT_HEALING = 0
        self.CURE_2 = 0
        self.BLESSING = 0
            # ARCHER
        self.STAGGERING_BLOW = 0
        self.FLAMY_ARROW = 0
        self.CHANCE_CAPTURE = 0
        self.MUSCLE_SOLIDATION = 0
        self.BLOW_UP_ARROW = 0
        self.POISON_ARROW = 0
        self.MYSTERIOUS_ARROW = 0
        self.NON_ATRI_ERSIST = 0
        self.HEARTH_BREAKER = 0
        self.LIFE_ABSORPTION = 0
        self.PAIN = 0
            # THIEF
        self.DOK = 0
        self.SPIN_ATTACK = 0
        self.CONFUSION = 0
        self.ARMOR_BREAKER = 0
        self.TWINBLADE_STRIKE = 0
        self.COUNTER_ATTACK = 0


class SkillCD(IntEnum):
        # ALL CLASSES
    BEHEADING = 700
    CONSUME_ITEM = 2100
        # KNIGHT
    ATTACK_KNIGHT_1H = 700
    ATTACK_KNIGHT_2H = 1400
    LIGHTENING_SLASH = 700  # wep speed
    TRANSCENDENTAL_BLOW = 4000  # 3300 + wep speed
    FLASHING_SLASH = 4000  # 3300 + wep speed
    MOCKERY = 60000
    UPWARD_SLASH = 700  # wep speed
    PROVOCATION = 5000
    INCREASING_CONCENTRATION = 90000
    WIDENING_WOUND = 700  # wep speed
    PROTECT = 1700
    SHIELD_ATTACK = 10000
    POWERFUL_UPWARD_SLASH = 6000  # 4600 + 2h wep speed
    BRUTAL_ATTACK = 700
    FORCE_OF_DEFENSE = 1205000
    CALL_OF_DEFENSE = 200000
    RUSH = 14000  # max
    SHIELD_OFFENSE = 50000
    CALL_OF_RECOVERY = 10000
    BERSERK = 185000
    HALF_SWING = 5000
    SACRIFICE = 40000
    CALL_OF_LIGHTNING_DEFENSE = 10000
    CALL_OF_ICE_DEFENSE = 10000
    CALL_OF_FIRE_DEFENSE = 10000
    CALL_OF_ON_TARGET_POINT = 10000
    CALL_OF_PHYSICAL_ATTACK = 10000
    SURVIVAL_INSTINCT = 600000
    ELASTIC_SHIELD = 600000
    REVIVAL = 40000
    PERFECT_DEFENSE = 150000 # ?
    SPIN_SLASH = 15500
    POWERFUL_WIDENING_WOUND = 700  # wep speed
    WALK_ON_AIR = 0  # ?
    SHOUT_OF_DEFENSE = 50000 # ?
    THE_BOOM_OF_EARTH = 100000 # ?
    SHOUT_OF_FIGHTING_SPIRIT = 200000 # ? max
    THE_WAVE_OF_EARTH = 200000 # ? max
        # MAGE
    BUFF_MEDITATION = 800000
    BUFF_DEF_INCANTATION = 900000
    LIGHT_MAGIC = 1200
    ICE_MAGIC = 1400
    FIRE_MAGIC = 1900  # less if fire mastery learned
    LIGHTENING_BLOW = 1400  # 1300
    SHOCK_WAVE = 1300
    SPLASHY_ICE = 1600
    FIRE_BLOW = 2800
    SPEED_UP = 2900
    GROUP_CURE = 1800
    LIGHTENING_SUMMONS = 1400
    HAIL = 1600
    FLAME_BOMB = 1900
    CURE_3 = 2100
    REFINING_WEAPON = 900000       
    SOULDESTRUCTION = 7200
    CHAIN_LIGHTENING = 2500
    THUNDER = 1600
    THUNDER_STORM = 184000
    ICE_RESTRICTION = 1400
    ICE_STORM = 184000
    EXPLOSION = 2000
    EXPLOSIVE_BURST = 4000
    FIRE_STORM = 184000
    BUFF_DEF = 600000
    BUFF_STR = 600000
    BUFF_HP = 600000
    BUFF_AGI = 600000
    BUFF_INT = 600000
    BUFF_CRIT = 600000
    PERFECT_CURE = 90000
    GROUP_CURE_2 = 1900
    PERFECT_GROUP_CURE_2 = 900000
    PERFECT_HEALING = 1800000
    CURE_2 = 2100
    BLESSING = 95000
        # Archer
    ATTACK_ARCHER = 800
    STAGGERING_BLOW = 3500
    CHANCE_CAPTURE = 900000
    MUSCLE_SOLIDATION = 900000
    MYSTERIOUS_ARROW = 5000
    FOCUSE_SHOOT = 5000
    POISON_ARROW = 1500
    LIFE_ABSORPTION = 6500
    PAIN = 31500
    NON_ATRI_RESIST = 900000
    FLAMY_ARROW = 800
    BLOW_UP_ARROW = 800
    HEARTH_BREAKER = 4500
        # THIEF
    ATTACK_THIEF = 500
    DOK = 40000
    SPIN_ATTACK = 20000
    CONFUSION = 300000
    ARMOR_BREAKER = 30000
    TWINBLADE_STRIKE = 600000
    COUNTER_ATTACK = 60000
        


class SkillMP(IntEnum):
        # KNIGHT
    LIGHTENING_SLASH = 20
    UPWARD_SLASH = 20
    TRANSCENDENTAL_BLOW = 38
    FLASHING_SLASH = 25
        
    MOCKERY = 10
    PROVOCATION = 36
    INCREASING_CONCENTRATION = 86
    WIDENING_WOUND = 20
    PROTECT = 50
    SHIELD_ATTACK = 58
    POWERFUL_UPWARD_SLASH = 32
    BRUTAL_ATTACK = 27
    FORCE_OF_DEFENSE = 380
    CALL_OF_DEFENSE = 0
    RUSH = 54
    SHIELD_OFFENSE = 136
    CALL_OF_RECOVERY = 0
    BERSERK = 290
    HALF_SWING = 94
    SACRIFICE = 0
    CALL_OF_LIGHTNING_DEFENSE = 0
    CALL_OF_ICE_DEFENSE = 0
    CALL_OF_FIRE_DEFENSE = 0
    CALL_OF_ON_TARGET_POINT = 0
    CALL_OF_PHYSICAL_ATTACK = 0
    SURVIVAL_INSTINCT = 0
    ELASTIC_SHIELD = 475
    REVIVAL = 400
    PERFECT_DEFENSE = 44
    SPIN_SLASH = 50
    POWERFUL_WIDENING_WOUND = 35
    WALK_ON_AIR = 0 # ?
    SHOUT_OF_DEFENSE = 0 # ?
    THE_BOOM_OF_EARTH = 0  # ?
    SHOUT_OF_FIGHTING_SPIRIT = 0 # ?
    THE_WAVE_OF_EARTH = 0 # ?
        # MAGES
    DEFENCE_INCANTATION = 82
    LIGHT_MAGIC = 7
    FIRE_MAGIC = 12
    ICE_MAGIC = 8
    LIGHTENING_BLOW = 22
    SHOCK_WAVE = 80
    SPLASHY_ICE = 73
    FIRE_BLOW = 62
    SPEED_UP = 0
    GROUP_CURE = 70
    LIGHTENING_SUMMONS = 30
    HAIL = 16
    FLAME_BOMB = 24
    CURE_3 = 51
    REFINING_WEAPON = 110        
    SOULDESTRUCTION = 106
    CHAIN_LIGHTENING = 174
    THUNDER = 46
    THUNDER_STORM = 352
    ICE_RESTRICTION = 126
    ICE_STORM = 396
    EXPLOSION = 40
    EXPLOSIVE_BURST = 142
    FIRE_STORM = 327
    BUFF_DEF = 103
    BUFF_STR = 128
    BUFF_HP = 114
    BUFF_AGI = 119
    BUFF_INT = 136
    BUFF_CRIT = 148
    PERFECT_CURE = 220
    GROUP_CURE_2 = 102
    PERFECT_GROUP_CURE_2 = 480
    PERFECT_HEALING = 596
    CURE_2 = 57
    BLESSING = 460
        # Archer
    STAGGERING_BLOW = 46
    CHANCE_CAPTURE = 56
    MUSCLE_SOLIDATION = 92
    MYSTERIOUS_ARROW = 64
    FOCUSE_SHOOT = 50
    POISON_ARROW = 15
    LIFE_ABSORPTION = 38
    PAIN = 72
    NON_ATRIBUTION_RESISTANCE = 50
    FLAMY_ARROW = 9  # for G5 flamy arrow
    BLOW_UP_ARROW = 17 # for G5
    HEARTH_BREAKER = 55
        # THIEF
    DOK = 120 # max grade
    SPIN_ATTACK = 175 # max grade
    CONFUSION = 70
    ARMOR_BREAKER = 185
    TWINBLADE_STRIKE = 65
    COUNTER_ATTACK = 195


class PimpTYPE(IntEnum):
    NONE = 0
    PHYSICAL_ATTACK = 1
    MAGICAL_ATTACK = 2
    TOA = 3
    TOD = 4
    DSS = 5
    QIGONG = 6