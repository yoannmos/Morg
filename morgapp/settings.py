"""
Setting file
"""
import json

SETTING_FILE = r"Morg\morgapp\morg_default_settings.json"
with open(SETTING_FILE) as config_file:
    SETTINGS = json.load(config_file)
