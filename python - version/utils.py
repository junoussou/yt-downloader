import os
import json
import subprocess
import interface

def get_bin_path(exe):
    """Retourne le chemin absolu vers un exécutable dans ../bin/"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bin_path = os.path.join(script_dir, "..", "bin", exe)
    if not os.path.isfile(bin_path):
        raise FileNotFoundError(f"{exe} introuvable")
    return bin_path

def create_download_folder(folder_name=""):
    """Crée le dossier de téléchargement, par défaut YT-DOWNLOADER dans les Téléchargements"""
    base_path = os.path.join(os.path.expanduser("~"), "Downloads", "YT-DOWNLOADER")
    if folder_name:
        full_path = os.path.join(base_path, folder_name)
    else:
        full_path = base_path

    os.makedirs(full_path, exist_ok=True)
    return full_path

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    if os.path.isfile(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def get_available_formats(url, yt_dlp_path):
    command = [yt_dlp_path, "-F", url]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Erreur lors de la récupération des formats :", e)
        return ""


def download(url, audio_only, destination, yt_dlp_path, format_code="best"):
    """Exécute yt-dlp pour télécharger l'URL selon le format choisi"""
    if audio_only == "a":
        command = [
            yt_dlp_path,
            "-x", "--audio-format", load_config().get("default_format"),
            "-o", os.path.join(destination, "%(title)s.%(ext)s"),
            url
        ]
    elif audio_only == "v":
        command = [
            yt_dlp_path,
            "-f", format_code,
            "-o", os.path.join(destination, "%(title)s.%(ext)s"),
            url
        ]
    else:
        raise ValueError("Type de téléchargement non supporté")

    subprocess.run(command, check=True)