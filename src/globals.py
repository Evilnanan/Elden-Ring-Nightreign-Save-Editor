from pathlib import Path
import os


# Global variables
WORKING_DIR = Path(os.path.dirname(os.path.abspath(__file__)))

# Items type
ITEM_TYPE_EMPTY = 0x00000000
ITEM_TYPE_WEAPON = 0x80000000
ITEM_TYPE_ARMOR = 0x90000000
ITEM_TYPE_RELIC = 0xC0000000

# Character names for vessel assignment
CHARACTER_NAME_ID = [100000, 100030, 100050, 100010, 100040, 100090,
                     100070, 100060, 110000, 110010]
CHARACTER_NAMES = ['Wylder', 'Guardian', 'Ironeye', 'Duchess', 'Raider',
                   'Revenant', 'Recluse', 'Executor', 'Scholar', 'Undertaker', 'All']

# Game Data Source Related
COLOR_MAP = ["Red", "Blue", "Yellow", "Green", "White"]
LANGUAGE_MAP = {
    "ar_AE": "العربية (الإمارات)",
    "de_DE": "Deutsch",
    "en_US": "English",
    "es_AR": "Español (Argentina)",
    "es_ES": "Español (España)",
    "fr_FR": "Français",
    "it_IT": "Italiano",
    "ja_JP": "日本語",
    "ko_KR": "한국어",
    "pl_PL": "Polski",
    "pt_BR": "Português (Brasil)",
    "ru_RU": "Русский",
    "th_TH": "ไทย",
    "zh_CN": "简体中文",
    "zh_TW": "繁體中文 (台灣)"
}
