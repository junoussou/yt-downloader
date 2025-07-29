import interface, utils, subprocess

def main():
    print("=== Téléchargeur YouTube (version Python) ===")

    try:
        yt_dlp = utils.get_bin_path(utils.load_config().get("yt_dlp_executable"))
    except FileNotFoundError as e:
        print(f"Erreur : {e}")
        return

    folder_name = interface.ask_for_folder()
    download_folder = utils.create_download_folder(folder_name)
    print(f"Dossier de destination : {download_folder}")

    url = interface.ask_for_url()
    choice = interface.ask_for_format()

    while choice is None:
        print("Choix invalide. Veuillez entrer 'a' pour audio ou 'v' pour vidéo.")
        choice = interface.ask_for_format()

    if choice == "a":
        try:
            utils.download(url, audio_only="a", destination=download_folder, yt_dlp_path=yt_dlp)
            print(f"✅ Téléchargement terminé ! dans {download_folder}")
        except subprocess.CalledProcessError:
            print("❌ Une erreur est survenue pendant le téléchargement.")
    elif choice == "v":
        try:
            utils.download(url, audio_only="v", destination=download_folder, yt_dlp_path=yt_dlp)
            print(f"✅ Téléchargement terminé ! dans {download_folder}")
        except subprocess.CalledProcessError:
            print("❌ Une erreur est survenue pendant le téléchargement.")

if __name__ == "__main__":
    main()