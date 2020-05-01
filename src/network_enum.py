"""
"""
from enum import IntEnum

class C2S(IntEnum):
    HEART_BEAT = 0x01
    CONNECT = 0x08
    ANS_CODE = 0x03
    LOGIN = 0x07
    LOAD_PLAYER = 0x04
    GAME_START = 0x0d
    SHORTCUT = 0x87
    UNKNOWN_LOGIN = 0xb7
    USE_SKILL = 0x75 # b, bd, bbd b=skill_id b=1 d=target_id | bbd=skill_id b=0 d=target_id (Blessing)
    USE_PICK = 0xae
    USE_ITEM = 0x40 # item_id
    ATTACK = 0x10  # BLL b=0x01 d=targetid d=z-coordinate
    MOVE = 0x5e # bbb d=ax b=ay b=az
    MOVE_STOP = 0x92 # bbb d=ax b=ay b=az
    LOG_OFF = 0x8c # b=0x01

    PARTY_REQUEST = 0x5a # d=id2
    PARTY_ACCEPT = 0x11 # bd, b=0x01 d=id2

    SELL_ITEM = 0x7d # dbdw d=npcid, b=0x01, d=itemid, w=amount
    DESTROY_ITEM = 0x61 # d=item_id

    SHOP = 0x35  #REGISTER ITEM bddd b=0, d=id, d=amount, d=price; REGISTER NAME bs b=2, s=name
    SHOP_OPEN = 0x20  # b b=0x01 open | b=0x00 close

    FISHING_START = 0x4e # d=0x480003 | bf: bbd b=1 b=0 d=0x23540064

    LOGIN_AFTER_LOAD = 0xfd

    SEND_MESSAGE = 0x38  # wssdwbdd w=0x100, s=message, s=toname, d=itemId, w=itemType, B=0x00, D=amount, D=price | b=0x02 to get list of recveived messages | bd b=0x0a, d=message_id accept message | bd b=0x09, d=message_id delete message | bd b=0x06, d=message_id read content
        
    OPEN_WOODENBOX = 0x9d # d=id
    CANCEL_OPEN_WOODENBOX = 0x16 #d=id

    BUY_AT_NPC = 0x78

    CHAT = 0x29 # b=0x40 (@), s=name+0x20+message (0x20=space)

    BLOB_CHANGE = 0xff  # d=5, d=1

    UPGRADE_ITEM = 0x19 # poli: d=item_id, d=pimp_item_id | attack talis: d=item_id, d=pimp_item_id, d=0
    APPLY_DSS = 0xb2  # "bddbwb",&Type, &IID, &ItemIndex, &JewelCheck, &Argument, &JewelAmount

    TELEPORT_REQUEST = 0xa0
    TELEPORT_SEND_Z = 0x79

class S2C(IntEnum):
    CHOOSE_CHARACTER_SCREEN = 0x11
    DELETED_CHARS = 0x19
    FRIEND_LIST = 0x12
    CHAR_INFORMATION = 0x1b
    LOAD_PLAYER_4 = 0xb2
    CONNECT = 0x2a
    LOGIN_ERROR = 0x2b
    LOAD_PLAYER_1 = 0x57
    LOAD_PLAYER_3 = 0x42
    LOAD_MAP_1 = 0x44
    LOAD_PLAYER_5 = 0x67
    LOAD_MAP_2 = 0x1c
    INVENTORY_ADD_ITEM = 0x07
    INVENTORY_REMOVE_ITEM = 0x08  # db d=id, b=0x0b?
    LOAD_EQUIP = 0x04  # after login
    INVENTORY_UPDATE_ITEM = 0x09 # dd d=id, d=new_amount
    CHAR_SKILL_INFO = 0x10
    CHAR_STATS = 0x42
    UNKNOWN_1 = 0x15    

    PLAYER_MOVE = 0x22
    PLAYER_MOVE_STOP = 0x23
    PLAYER_EFFECT_1 = 0x47
    PLAYER_EFFECT_2 = 0x48
    ATTACK_SOMEONE_PHYSICAL = 0x3e
    PLAYER_APPEAR = 0x32
    PLAYER_DISAPPEAR = 0x37
    PLAYER_UPDATE_INFO = 0x45  # ?
    PLAYER_USE_ITEM = 0x49
    UNKNOWN_2 = 0x94  # ?
    MESSAGE = 0x13
    UPDATE_MPROPERTY = 72

    MOB_APPEAR = 0x33
    MOB_DISAPPEAR = 0x38
    UNKNOWN_3 = 0x3f
    MOB_PLAYER_STATE = 0x3d
    MOB_MOVE = 0x24
    MOB_MOVE_STOP = 0x25

    DROP_APPEAR = 0x36
    DROP_DISAPPEAR = 0x3b

    NPC_APPEAR = 0x34
    NPC_DISAPPEAR = 0x39

    PING = 0x1e

    NOTICE_1 = 0x0f
    NOTICE_2 = 0xff
    CHAT = 0x3c

    PARTY_REQUEST = 0x52
    PARTY_INFO = 0x54 # b=partysize, dsbbww d=id,s=name,b=class,b=level,w=curhp,w=maxhp
    PARTY_HEALTH_UPDATE = 0x55  # dbdd d=id, b=type(hp=0x07,..), d=cur, d=max
    PARTY_POSITION_UPDATE = 0x53 # b+ddd+... b=partysize, d=id, d=x, d=y

    WOODENBOX_OPEN = 0x43

    ITEM_UPDATE_INFO = 0x5c  #

    MD5_PACKET = 0xff

    TELEPORT_REQUEST_Z = 0x46
    TELEPORT_DONE = 0x16
