import os
import shutil
import subprocess
import tempfile
import time
import webbrowser
from ctypes import windll
from zipfile import ZipFile
from pydub import AudioSegment
from pydub.playback import play

import minecraft_launcher_lib as mll
import requests

from config import mcu_appdata, current_mc_version_string, mc_folder, neoforge_installer_download_url, \
    java_runtime_path, launcher_profiles_json_var, mods_download_url, folder_in_mcu_download_zip, mc_custom_temp_folder, \
    neoforge_installer_var, mods_downloaded_var, mods_extr_folder_var, program_path


def CreateMBox(title_b: str, text_b: str, variant_b: int):
    windll.user32.MessageBoxW(0, title_b, text_b, variant_b)


def run_contact_tab(url):
    webbrowser.open_new_tab(url)


current_max = 0


def play_background_audio():
    mcu_song_1_melody = AudioSegment.from_wav(program_path + "\\music\\piano.wav")
    mcu_song_1_full = AudioSegment.from_wav(program_path + "\\music\\piano2.wav")
    mcu_song_2_melody = AudioSegment.from_wav(program_path + "\\music\\piano3.wav")
    mcu_song_1_full = AudioSegment.from_wav(program_path + "\\music\\piano4.wav")

    mcu_song_1_melody_lower = mcu_song_1_melody - 20
    mcu_song_1_full_lower =  mcu_song_1_full - 20
    mcu_song_2_melody_lower = mcu_song_2_melody - 20
    mcu_song_1_full_lower = mcu_song_1_full - 20


    time.sleep(2)
    play(mcu_song_1_melody_lower)
    time.sleep(3)
    play(mcu_song_1_full_lower)
    time.sleep(3)
    play(mcu_song_2_melody_lower)
    time.sleep(3)
    play(mcu_song_1_full_lower)













def mcu_initial_install(progress_bar_name):
    time.sleep(2)
    print("initial install started")

    if os.path.exists(mcu_appdata):
        pass
    else:
        os.makedirs(mcu_appdata)
        os.makedirs(mc_folder)
        if not os.path.isdir(mc_custom_temp_folder):
            os.makedirs(mc_custom_temp_folder)
        #os.makedirs(mcu_temp_folder)

    def instl_set_status(status: str):
        print(status)

    def instl_set_progress(progress: int):
        if current_max != 0:
            print(f"{progress}/{current_max}")

    def instl_set_max(new_max: int):
        global current_max
        current_max = new_max

    instl_callback = {
        "setStatus": instl_set_status,
        "setProgress": instl_set_progress,
        "setMax": instl_set_max
    }

    progress_bar_name.set(0.1)

    print("download würde jetzt starten")
    #time.sleep(20)
    mll.install.install_minecraft_version(current_mc_version_string, mc_folder, instl_callback)
    print("Library's installed")
    print("Minecraft Vanilla 1.21.1 installed")
    print("Java Runtime Installed")

    with open(launcher_profiles_json_var, "w") as f:
        f.write("{}")
        f.close()

    neoforge_installer_url_response = requests.get(neoforge_installer_download_url, allow_redirects=True, stream=True)
    with open(neoforge_installer_var, "wb") as f:
        f.write(neoforge_installer_url_response.content)
        f.close()

    subprocess.run([java_runtime_path, "-jar", neoforge_installer_var, "--installClient", mc_folder])

    print("NeoForged Installed")

    progress_bar_name.set(0.3)


    mod_download_response = requests.get(mods_download_url, allow_redirects=True, stream=True)
    with open(mods_downloaded_var, "wb") as f:
        f.write(mod_download_response.content)
        f.close()

    ZipFile(mods_downloaded_var, "r").extractall(mc_custom_temp_folder)

    shutil.copytree(mods_extr_folder_var, mc_folder, dirs_exist_ok=True)


    progress_bar_name.set(0.7)

















