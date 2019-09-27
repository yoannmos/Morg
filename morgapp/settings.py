"""
Setting file
"""
import json

SETTING_FILE = r"D:\PythonWorkspace\Python_Project\Morg\morg_default_settings.json"
with open(SETTING_FILE) as config_file:
    SETTINGS = json.load(config_file)


if __name__ == "__main__":
    print(SETTINGS)
