

def ask_for_folder():
    return input("Nom du dossier (laisser vide pour le dossier par défaut) : ").strip()

def ask_for_url():
    return input("URL YouTube de la vidéo ou playlist : ").strip()

def ask_for_format():
    choice = input("Audio ou Vidéo ? ('a' pour audio / 'v' pour vidéo) : ").strip().lower()
    return choice if choice in ["a", "v"] else None