chcp 65001
@echo off
setlocal

echo === Téléchargeur YouTube avec yt-dlp ===

if not exist "yt-dlp.exe" (
    echo Erreur : yt-dlp.exe introuvable. Veuillez le placer dans le même dossier que ce script.
    pause
    exit /b
)

:: Vérifier si le dossier de téléchargement existe, sinon le créer
if not exist "%USERPROFILE%\Downloads\YT-DOWNLOADER" (
    mkdir "%USERPROFILE%\Downloads\YT-DOWNLOADER"
    if errorlevel 1 (
        echo Erreur lors de la création du dossier. Veuillez vérifier les permissions.
        pause
        exit /b
    )
)

:: Obtenir le chemin du dossier par défaut
set "defaultFolder=%USERPROFILE%\Downloads\YT-DOWNLOADER"

:: Demander à l'utilisateur le nom du dossier (optionnel)
set /p foldername="Nom du dossier (laisser vide pour le dossier par défaut) : "

:: Utiliser le dossier par défaut si aucun nom n’a été donné
if "%foldername%"=="" (
    set "foldername=%defaultFolder%"
) else (
    :: Vérifier si le dossier existe, sinon le créer
    if not exist "%USERPROFILE%\Downloads\YT-DOWNLOADER\%foldername%" (
        mkdir "%USERPROFILE%\Downloads\YT-DOWNLOADER\%foldername%"
        if errorlevel 1 (
            echo Erreur lors de la création du dossier. Veuillez vérifier les permissions.
            pause
            exit /b
        )
    )
    set "foldername=%USERPROFILE%\Downloads\YT-DOWNLOADER\%foldername%"
)

echo Dossier de destination : %foldername%

:: Demander l'URL
set /p url="URL YouTube de la vidéo ou playlist : "

:: Demander si l'utilisateur veut l'audio ou la vidéo
set /p choice="Audio ou Video ? (Tapez 'a' pour Audio ou 'v' pour Video) : "


:: Vérifier le choix
if /i "%choice%"=="a" (
    echo Téléchargement de(s^) audio(s^) en cours...
    yt-dlp.exe -x --audio-format mp3 -o "%foldername%\%%(title)s.%%(ext)s" "%url%"
    echo Téléchargement terminé dans le dossier : %foldername%
) else if /i "%choice%"=="v" (
    echo Téléchargement de(s^) vidéo(s^) en cours...
    yt-dlp.exe -f best -o "%foldername%\%%(title)s.%%(ext)s" "%url%"
    echo Téléchargement terminé dans le dossier : %foldername%
) else (
    echo Choix invalide. Veuillez relancer le script.
)
echo Merci d’avoir utilisé notre Téléchargeur YouTube !
explorer "%foldername%"
pause