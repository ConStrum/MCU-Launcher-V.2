
from os import path
from pathlib import Path



CURRENT_APP_VERSION = "Alpha-0.1"
APP_TITLE = 'MCU Launcher'
PLACEHOLDER_TEXT = "Placeholder Text"



M_WINDOW_SIZE = "1280x720"
M_WINDOW_SIZE_X = int(M_WINDOW_SIZE[:4])
M_WINDOW_SIZE_Y = int(M_WINDOW_SIZE[5:])



MICROSOFT_CLIENT_ID = "d3a19c4d-0b0f-4fe6-a0ec-c7588945d96a"
MICROSOFT_REDIRECT_URI = "https://login.microsoftonline.com/common/oauth2/nativeclient"



FIRST_WINDOW_SIZE = "250x350"
FIRST_WINDOW_SIZE_X = int(FIRST_WINDOW_SIZE[:3])
FIRST_WINDOW_SIZE_Y = int(FIRST_WINDOW_SIZE[4:])



program_path = path.dirname(path.realpath(__file__))
user_folder = str(Path.home())
mcu_appdata = user_folder + "\\AppData\\Local\\MCULauncher2"
fully_installed_file = mcu_appdata + "\\fully_installed.txt"

custom_config_file = mcu_appdata + "\\custom_config.ini"




contact_url = 'https://construm.de/kontakt/'


pre_text_error = """Hallo Liebes Entwickler Team,

Mir ist folgender Fehler aufgetreten (siehe Error-Log).

Hier bitte weitere Infos ergänzen.
"""


error_info_text_box = "Ein schwerwiegender Fehler ist aufgetreten, der leider nicht behoben werden konnte. Links findest du die Fehlerbeschreibung. Du hast außerdem die Möglichkeit, uns diesen Fehler zu melden, damit wir ihn schnellstmöglich beheben können."



###MC###

mc_folder = mcu_appdata + "\\.minecraft"
mc_custom_temp_folder = mcu_appdata + "\\TEMP"
mc_user_folder = mcu_appdata + "\\mc_user"

current_mc_version_string = "1.21.1"

neoforge_installer_download_url = 'https://maven.neoforged.net/releases/net/neoforged/neoforge/21.1.72/neoforge-21.1.72-installer.jar'
mods_download_url = 'https://github.com/ConStrum/mcupackage/archive/refs/heads/main.zip'

java_runtime_path = mc_folder + "\\runtime\\java-runtime-delta\\windows-x64\\java-runtime-delta\\bin\\java.exe"

launcher_profiles_json_var = mc_folder + "\\launcher_profiles.json"
neoforge_installer_var = mc_custom_temp_folder + "\\neoforge.jar"

mods_downloaded_var = mc_custom_temp_folder + "\\mcu.zip"
mods_extr_folder_var = mc_custom_temp_folder + "\\mcupackage-main"

sound_activated_after_launcher_start = True



folder_in_mcu_download_zip = "mcupackage-main"














