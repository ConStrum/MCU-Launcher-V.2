from zipfile import ZipFile
import tempfile
import requests
from config import neoforge_installer_download_url, mc_folder, mods_download_url
import shutil
import os

response = requests.get(mods_download_url)
zip_temp_file = tempfile.NamedTemporaryFile(mode="w+b", delete=False)  # Datei nicht sofort löschen
zip_temp_file.write(response.content)
zip_temp_file.close()  # Schließe die Datei, um sie später zu verwenden

try:
    with tempfile.TemporaryDirectory() as extr_temp_zip:
        with ZipFile(zip_temp_file.name) as zip_file:
            zip_file.extractall(extr_temp_zip)  # Entpacke in das Verzeichnis

        os.makedirs(mc_folder, exist_ok=True)  # Stelle sicher, dass Zielordner existiert
        for file_name in os.listdir(extr_temp_zip):
            src_path = os.path.join(extr_temp_zip, file_name)
            dst_path = os.path.join(mc_folder, file_name)
            shutil.copy(src_path, dst_path)  # Kopiere Dateien
finally:
    os.remove(zip_temp_file.name)  # Lösche die temporäre Datei
