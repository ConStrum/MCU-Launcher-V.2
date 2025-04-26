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
import configparser
import webview
import json
from PIL import Image

import minecraft_launcher_lib as mll
import requests

from default_config import mcu_appdata, current_mc_version_string, mc_folder, neoforge_installer_download_url, \
    java_runtime_path, launcher_profiles_json_var, mods_download_url, folder_in_mcu_download_zip, mc_custom_temp_folder, \
    neoforge_installer_var, mods_downloaded_var, mods_extr_folder_var, program_path, custom_config_file, \
    sound_activated_after_launcher_start, MICROSOFT_CLIENT_ID, MICROSOFT_REDIRECT_URI, mc_user_folder


def CreateMBox(title_b: str, text_b: str, variant_b: int):
    windll.user32.MessageBoxW(0, title_b, text_b, variant_b)


def run_contact_tab(url):
    webbrowser.open_new_tab(url)

def Main_Window_Run_Protocol():
    print("Main Window Stopping.")


def create_default_config(config_path: str):
    config = configparser.ConfigParser()


    config.add_section('DEBUG')
    config['DEBUG']['debug_mode'] = 'False'


    with open(config_path, 'w') as configfile:
        config.write(configfile)


def retrieve_config_argument_to_file(config_path, section, option):
    try:
        config = configparser.ConfigParser()

        config.read(config_path)

        return config.get(section, option)
    except Exception as e:
        return None


def add_config_argument_to_file(config_path, section: str, option: str, value: str):
    if not os.path.isfile(config_path):
        create_default_config(config_path)
    config = configparser.ConfigParser()
    config.read(config_path)

    if not config.has_section(section):
        config.add_section(section)


    config.set(section, option, value)

    with open(config_path, 'w') as configfile:
        config.write(configfile)
    


def play_background_audio(play_audio_flag: bool = False):
    if play_audio_flag:
        print("Playing background audio ...")
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
    else:
        print("Playing background audio skipped.")




redirected_url = None

def do_microsoft_login(top_level_class, login_complete: bool):
    global redirected_url

    if login_complete:
        shutil.rmtree(mc_user_folder)
        

    if not login_complete:
        print("Doing Microsoft Login...")

        login_url, gen_state, code_verifier = mll.microsoft_account.get_secure_login_data(MICROSOFT_CLIENT_ID, MICROSOFT_REDIRECT_URI)




        login_window = webview.create_window("Microsoft Login", login_url)
        def login_window_on_change():
            try:
                global redirected_url
                print(login_window.get_current_url())
                while True:
                    time.sleep(0.2)
                    if "nativeclient?code" in login_window.get_current_url():
                        redirected_url = login_window.get_current_url()
                        login_window.destroy()
                        break
            except Exception:
                pass

        webview.start(func=login_window_on_change)

        try:
            auth_code = mll.microsoft_account.parse_auth_code_url(redirected_url, gen_state)
        except AssertionError:
            print("States do not match.")
            raise Exception("States do not match.")
        except KeyError:
            print("Url not valid.")
            raise Exception("Url not valid.")

        mc_login_data = mll.microsoft_account.complete_login(MICROSOFT_CLIENT_ID, None, MICROSOFT_REDIRECT_URI, auth_code, code_verifier)

        with open(mc_user_folder + "\\mc_login_data.json", "w") as f:
            json.dump(mc_login_data, f, indent=4)
            f.close()

        with open (mc_user_folder + "\\access_token.dat", "w") as f:
            f.write(mc_login_data["access_token"])
            f.close()

        with open (mc_user_folder + "\\refresh_token.dat", "w") as f:
            f.write(mc_login_data["refresh_token"])
            f.close()

        mc_skin_url = mc_login_data["skins"][0]["url"]

        skin_file_response = requests.get(mc_skin_url)

        with open(mc_user_folder + "\\skinfile.png", "wb") as f:
            f.write(skin_file_response.content)
            f.close()


        skin_file_pil = Image.open(mc_user_folder + "\\skinfile.png").convert('RGBA')
        face_box = (8, 8, 16, 16)
        overlay_box = (40, 8, 48, 16)
        face_pil = skin_file_pil.crop(face_box)


        overlay_pil = skin_file_pil.crop(overlay_box)

        face_pil.paste(overlay_pil, (0, 0), overlay_pil)

        scaled_face = face_pil.resize(
            (face_pil.width * 8, face_pil.height * 8),
            Image.NEAREST
        )

        scaled_face.save(mc_user_folder + "\\player_head.png")
        scaled_face.save(mc_user_folder + "\\player_head.ico", format="ICO")

        top_level_class.iconbitmap(mc_user_folder + "\\player_head.ico")

        uuid_mc = mc_login_data["id"]

        skin_render_3d_url = f"https://crafatar.com/renders/body/{uuid_mc}?overlay=true&default=MHF_Steve"

        skin_render_3d_response = requests.get(skin_render_3d_url)
        with open(mc_user_folder + "\\skin_render_3d.png", "wb") as f:
            f.write(skin_render_3d_response.content)
            f.close()
















current_max = 0
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

















