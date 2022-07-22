# 🚀 A tool to set-up Windows 10 faster and easier
# 💬 All the download links are from the original sites.

# 📝 Simple program yet useful for lazy people
# 😗 Sorry for the messy code.. But hey it works!
# ❗ We will never ask you to use an obfuscated file, for your own safety.

# ⚡ Import needs
from asyncio.windows_events import NULL
import ctypes
from shutil import which
from ssl import SO_TYPE
from tarfile import NUL
from colorama import Fore, Back, Style
import requests
import sys
import shutil
import time
import os
import zipfile
import subprocess
import webbrowser

# ⚡ Initialize colorama
from colorama import init
init()

# ⚡ Variables
startfast = "n"
rainmeterinstalled = "n"
rainmeterdifdir = "n"
skinsinstalled = "n"
allRMSkinsInstalled = "n"
username = os.getlogin()


# 💋 Windows clear terminal
def cls():
    os.system('cls')
def Done():
    os.system("taskkill /f /im explorer.exe")
    os.system("explorer.exe")
    print(Style.RESET_ALL)
    print("[*] You might need to drag some skins in rainmeter, but the rest is done successfully!.")
    print("[v] All done, restart your computer to see more changes.")

# 📝 Print
def printLogInstallBasics():
    print("[>] Download rainmeter (2,35 MB)")
    print("[>] Install rainmeter (~6 MB)")
    print("[>] Download and apply rainmeter skins (~2 MB)")
    print("[>] Install useful chrome extensions (~10 MB)")
    print("[>] Debloat windows (~-0,5 GB)")
    print(Style.RESET_ALL)

# 📝 Confirm
def beginOrNah():
    print("[?] Do you want to begin?")
    x = str(input("[>] Y/n: "))
    print(Style.RESET_ALL)
    if x == "" or x == " " or x == "y" or x == "Y" or x == "yes" or x == "Yes" or x == "YES":
        print("(LOG) Starting (x (STR) = " + x + ")")
        print("[*] Okay! Please wait while we are loading needs (This shouldnt take long)")
        Basics(str(sys.argv[1])) # Either dark or light mode.
        os._exit(0)
    if x != "" or x != " " or x != "y" or x != "Y" or x != "yes" or x != "Yes" or x != "YES":
        print("(LOG) Quiting program. (x (STR) = " + x + ")")
        print("[/] Okay, see you next time :)")
        os._exit(0)

# 🙂 Start of installation
def Basics(mode):
    #Fix UNBOUND LOCAL ERROR
    rainmeterdifdir = "x"
    rainmeterinstalled = "x"
    skinsinstalled = "x"
    allRMSkinsInstalled = "x"
    # Start
    cls()
    print(Style.RESET_ALL)

    print(Fore.WHITE + "       A tool to set-up Windows 10 faster and easier")
    print("               Last updated " + Fore.CYAN + "2022 July 19")

    print(Style.RESET_ALL)


    print("Setting your machine up in " + mode + " mode")
    print(Style.RESET_ALL)

    if os.path.exists("cache"):
        print("[-] Removing previous cache")
        shutil.rmtree("cache")
    os.mkdir("cache")
    print("[+] Created cache folder in current directory")

    print("[..] Downloading wallpaper.")
    if mode == "light":
        open('cache/wallpaper.jpg', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/1000039037412835328/paula-vermeulen-_f2m3mEkaaU-unsplash.jpg', allow_redirects=True).content)
    else:
        open('cache/wallpaper.jpg', 'wb').write(requests.get('https://images.hdqwalls.com/download/macos-mojave-night-mode-stock-0y-1920x1080.jpg', allow_redirects=True).content)
    
    time.sleep(0.75)

    print("[.] Setting up wallpaper")
    pathToWallpaper = os.path.normpath(os.getcwd() + "/cache/wallpaper.jpg")
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, pathToWallpaper, 0)
    print("[v] Wallpaper set up")

    if mode == "dark":
        print("[..] Downloading file to set up dark mode")
        open('cache/dark-theme.reg', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/1000049560367931422/dark-theme.reg', allow_redirects=True).content) 
        print("[.] Downloaded, running file silently")
        os.system('regedit /s cache/dark-theme.reg')
        print("[v] Apps now run in dark mode")
    else:
        print("[..] Downloading file to set up light mode")
        open('cache/light-theme.reg', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/1000051900315619459/light-theme.reg', allow_redirects=True).content) 
        print("[.] Downloaded, running file silently")
        os.system('regedit /s cache/light-theme.reg')
        print("[v] Apps now run in light mode")

    print("[..] Checking if Rainmeter is installed.")
    print(Fore.LIGHTWHITE_EX + "(LOG) CHECKING IN C:\Program Files\Rainmeter" + Style.RESET_ALL)
    
    time.sleep(0.5)

    if not os.path.exists("C:\Program Files\Rainmeter"):
        print("[!] Rainmeter is not installed.")
        print("[..] Downloading rainmeter.")
        if str(sys.argv[2]) == "winget":
            print("[.] Installing via WINGET, this wont be fully automatic.")
            os.system('winget install Rainmeter')
            print("[v] Rainmeter installed via WINGET")
        else:
            print("[..] Downloading rainmeter via requests.")
            open('cache/rainmeter.exe', 'wb').write(requests.get('https://github.com/rainmeter/rainmeter/releases/download/v4.5.13.3632/Rainmeter-4.5.13.exe', allow_redirects=True).content) 
            print("[.] Installing rainmeter silently.")
            os.system(os.getcwd() + '/cache/rainmeter.exe /S')
            print("[v Rainmeter installed via requests.")
    else:
        print("[v] Rainmeter is installed.")
        rainmeterinstalled = "y"
        print(Fore.LIGHTWHITE_EX + "(LOG) CHECKING IF RAINMETER SKINS ALREADY INSTALLED" + Style.RESET_ALL)
        if not os.path.exists("C:/Users/" + username + "/Documents/Rainmeter/Skins/TranslucentTaskbar"):
            print("[!] Skins not found.")
            skinsinstalled = "n"
        else:
            print("[v] TranslucentTaskbar found.")
            if not os.path.exists("C:/Users/" + username + "/Documents/Rainmeter/Skins/TaskbarX"):
                print("[!] Skins not found.")
                skinsinstalled = "n"
            else:
                print("[v] TaskbarX found.")
                if not os.path.exists("C:/Users/" + username + "/Documents/Rainmeter/Skins/Simplistic Clock"):
                    print("[!] Skins not found.")
                    skinsinstalled = "n"
                else:
                    print("[v] Simplistic Clock found.")
                    skinsinstalled = "y"
                    allRMSkinsInstalled = "y"
            skinsinstalled = "y"


    if allRMSkinsInstalled == "y":
        print("[v] Nice! All rainmeter skins are already installed.")
    else:
        print("[..] Downloading pre-set rainmeter skins")
        open('cache/rainmeter-skins.zip', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/1000058087274709032/Rainmeter.zip', allow_redirects=True).content)
        print("[.] Unzipping pre-set rainmeter skins")
        with zipfile.ZipFile("cache/rainmeter-skins.zip", 'r') as zip_ref:
            zip_ref.extractall("cache")
        try:
            shutil.move("cache/Rainmeter", "C:/Users/" + username + "/Documents")
        except:
            print("[!] Error encountered while trying to move rainmeter skins, trying again")
            shutil.rmtree("C:/Users/" + username + "/Documents/Rainmeter")
            print("[-] Removed rainmeter skins directory")
            shutil.rmtree("cache/Rainmeter")
            print("[-] Removed cached unzipped rainmeter skins directory")
            print("[.] Unzipping pre-set rainmeter skins")
            with zipfile.ZipFile("cache/rainmeter-skins.zip", 'r') as zip_ref:
                zip_ref.extractall("cache")
            shutil.move("cache/Rainmeter", "C:/Users/" + username + "/Documents")
        print("[v] Installed rainmeter skins successfully (Not set up yet)")

    print("[......] Configuring rainmeter skins (This might take a while)")
    print("[.....] TaskbarX already set, no need for changes")
    print("[....] TranslucentTaskbar already set, no need for changes")
    print("[...] TranslucentTaskbar already set, no need for changes")
    print("[..] Reading Just A Bin ini")

    if mode=="dark":
        file = open("C:/Users/" + username + "/Documents/Rainmeter/Skins/Just A Bin/Just A Bin.ini", "r")
        replacement = ""
        for line in file:
            line = line.strip()
            changes = line.replace("IconEmpty=#@#Empty_B.png", "IconEmpty=#@#Empty.png")
            replacement = replacement + changes + "\n"

        file.close()
        fout = open("C:/Users/" + username + "/Documents/Rainmeter/Skins/Just A Bin/Just A Bin.ini", "w")
        fout.write(replacement)
        fout.close()
        file2 = open("C:/Users/" + username + "/Documents/Rainmeter/Skins/Just A Bin/Just A Bin.ini", "r")
        replacement2 = ""
        for line2 in file2:
            line2 = line2.strip()
            changes2 = line2.replace("IconFull=#@#Full_B.png", "IconFull=#@#Full.png")
            replacement2 = replacement2 + changes2 + "\n"
        file2.close()
        fout2 = open("C:/Users/" + username + "/Documents/Rainmeter/Skins/Just A Bin/Just A Bin.ini", "w")
        fout2.write(replacement2)
        fout2.close()

    time.sleep(0.5)
    print("[v] Successfully wrote into Just A Bin")
    time.sleep(0.1)

    print("[.] Reading Simplistic Clock ini")
    print("[v] Simplistic Clock already set, no need for changes")

    print("[..] Creating layout")
    
    time.sleep(0.5)

    try:
        shutil.rmtree("C:/Users/" + username + "/AppData/Roaming/Rainmeter/Layouts")
        time.sleep(0.5)
        os.mkdir("C:/Users/" + username + "/AppData/Roaming/Rainmeter/Layouts/RainmeterLYT")
    except:
        try:
            shutil.rmtree("C:/Users/" + username + "/AppData/Roaming/Rainmeter/Layouts")
            time.sleep(1)
            os.makedirs("C:/Users/" + username + "/AppData/Roaming/Rainmeter/Layouts/RainmeterLYT")
            os.mkdir("C:/Users/" + username + "/AppData/Roaming/Rainmeter/Layouts/RainmeterLYT")
        except:
            print("[!] Something errored, ignoring..")

    print("[.] Created folder, downloading layout file")
    time.sleep(0.5)
    try:
        open('C:/Users/' + username + '/AppData/Roaming/Rainmeter/Layouts/RainmeterLYT/Rainmeter.ini', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/1000086310360457277/Rainmeter.ini', allow_redirects=True).content)
    except:
        print("[!] Couldnt make layout file, ignoring.. (You might need to apply the skins your own..)")
    
    print("[v] Layout set (RainmeterLYT)")

    print("[*] Restarting rainmeter cleanly (This shouldnt take long)")

    subprocess.call(["C:/Program Files/Rainmeter/Rainmeter.exe", "!LoadLayout", "RainmeterLYT"])
    os.system("C:/Program Files/Rainmeter/Rainmeter.exe !Refresh")
    os.system("C:/Program Files/Rainmeter/Rainmeter.exe !Update")
    os.system("C:/Program Files/Rainmeter/Rainmeter.exe !Load")
    os.system("taskkill /f /im rainmeter.exe")
    os.system("C:/Program Files/Rainmeter/Rainmeter.exe")
    os.system("C:/Program Files/Rainmeter/Rainmeter.exe !LoadLayout RainmeterLYT")

    print(Style.RESET_ALL)
    
    print(Fore.GREEN + "[v] RAINMETER AND STYLING DONE")

    print(Style.RESET_ALL)
    print(Style.RESET_ALL)
    
    print(Fore.GREEN + "[v] Set wallpaper")
    print("[v] Download rainmeter")
    print("[v] Install rainmeter")
    print("[v] Download and apply rainmeter skins" + Fore.WHITE)
    print("[>] Install useful chrome extensions")
    print("[*] Debloat windows")

    print(Style.RESET_ALL)

    print("[*] You will be redirected to alot of sites to install some chrome extensions (This cant be automated)")
    print("[*] Just press install extension to set up chrome perfectly.")

    print(Style.RESET_ALL)

    print("[*] Loading sites..")

    time.sleep(2)

    os.system("start https://chrome.google.com/webstore/detail/enhancer-for-youtube/ponfpcnoihfmfllpaingbgckeeldkhle?hl=en")
    os.system("start https://chrome.google.com/webstore/detail/sponsorblock-for-youtube/mnjggcdmjocbbbhaepdhchncahnbgone?hl=en")
    os.system("start https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=en")
    os.system("start https://chrome.google.com/webstore/detail/return-youtube-dislike/gebbhagfogifgggkldgodflihgfeippi")
    os.system("start https://chrome.google.com/webstore/detail/fasterweb/nmgpnfccjfjhdenioncabecepjcmdnjg")
    print("https://chrome.google.com/webstore/detail/enhancer-for-youtube/ponfpcnoihfmfllpaingbgckeeldkhle?hl=en")
    print("https://chrome.google.com/webstore/detail/sponsorblock-for-youtube/mnjggcdmjocbbbhaepdhchncahnbgone?hl=en")
    print("https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=en")
    print("https://chrome.google.com/webstore/detail/return-youtube-dislike/gebbhagfogifgggkldgodflihgfeippi")
    print("https://chrome.google.com/webstore/detail/fasterweb/nmgpnfccjfjhdenioncabecepjcmdnjg")

    print("[*] Sites loaded")

    time.sleep(0.25)

    print(Style.RESET_ALL)
    print(Style.RESET_ALL)
    
    print(Fore.GREEN + "[v] Set wallpaper")
    print("[v] Download rainmeter")
    print("[v] Install rainmeter")
    print("[v] Download and apply rainmeter skins")
    print("[v] Install useful chrome extensions" + Fore.WHITE)
    print("[>] Debloat windows")
    print(Style.RESET_ALL)
    print("[*] Lots of people dont trust debloating software, but we will be debloating your PC safely.") 
    print(Style.RESET_ALL)
    print("[*] This will be cleaned and debloated:")    
    print("[>] Temp files")    
    print("[>] Block ads")    
    print("[>] Add Take Ownership to Context Menu")    
    print("[>] Remove cortana")     
    print("[>] Fix privacy")    
    print("[>] Remove Telemetry and Remove Data Collection")
    print("[>] Explorer fixes and tweaks")
    print("[>] Remove suggestions in start menu")
    print(Style.RESET_ALL)
    x = str(input("[>] Continue? [Y/n]: "))
    print(Style.RESET_ALL)
    if x == "" or x == " " or x == "y" or x == "Y" or x == "yes" or x == "Yes" or x == "YES":
        print("[*] Deleting Temp files")   
        dir = 'C:/Users/' + username + '/AppData/Local/Temp'
        for f in os.listdir(dir):
            try:
                os.remove(os.path.join(dir, f)) 
            except:
                pass

        print("[*] Block ads")   
        open('cache/block-ads.ps1', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/1000094770917544066/block-ads.ps1', allow_redirects=True).content)
        os.system("powershell -File cache/block-ads.ps1")

        print("[*] Add Take Ownership to Context Menu") 
        open('cache/Add_Take_Ownership_to_Context_menu.reg', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/1000098254358319205/Add_Take_Ownership_to_Context_menu.reg', allow_redirects=True).content)
        os.system('regedit /s cache/Add_Take_Ownership_to_Context_menu.reg')
        open('cache/zipAltMenu.reg', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/1000098695250972673/7-zip_Alternate_Context_Menu_1.reg', allow_redirects=True).content)
        os.system('regedit /s cache/zipAltMenu.reg')

        try:
            print("[*] Remove cortana")   
            os.system("taskkill /F /IM SearchUI.exe")
            os.system('move "%windir%\\SystemApps\\Microsoft.Windows.Cortana_cw5n1h2txyewy" "%windir%\\SystemApps\\Microsoft.Windows.Cortana_cw5n1h2txyewy.bak"')
            os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search" /v "AllowCortana" /t REG_DWORD /d 0')

            print("[*] Fix privacy")   
            os.system('reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo" /v Enabled /t REG_DWORD /d 0 /f')
            os.system('reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\AppHost" /v EnableWebContentEvaluation /t REG_DWORD /d 0 /f')
            os.system('reg add "HKCU\\Control Panel\\International\\User Profile" /v HttpAcceptLanguageOptOut /t REG_DWORD /d 1 /f')

            print("[*] Remove Telemetry and Remove Data Collection")   
            os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Device Metadata" /v PreventDeviceMetadataFromNetwork /t REG_DWORD /d 1 /f')
            os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d 0 /f')
            os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\MRT" /v DontOfferThroughWUAU /t REG_DWORD /d 1 /f')
            os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\SQMClient\\Windows" /v "CEIPEnable" /t REG_DWORD /d 0 /f')
            os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat" /v "AITEnable" /t REG_DWORD /d 0 /f')
            os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\AppCompat" /v "DisableUAR" /t REG_DWORD /d 1 /f')
            os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v "AllowTelemetry" /t REG_DWORD /d 0 /f')
            os.system('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\AutoLogger\\AutoLogger-Diagtrack-Listener" /v "Start" /t REG_DWORD /d 0 /f')
            os.system('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\WMI\\AutoLogger\\SQMLogger" /v "Start" /t REG_DWORD /d 0 /f')

            print("[*] Explorer fixes and tweaks")   
            os.system('reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v "LaunchTo" /t REG_DWORD /d 1 /f')
            os.system('reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v "Hidden" /t REG_DWORD /d 1 /f')
            os.system('reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v "ShowSuperHidden" /t REG_DWORD /d 1 /f')
            os.system('reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v "HideFileExt" /t  REG_DWORD /d 0 /f')

            print("[*] Remove suggestions in start menu")   
            os.system('reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" /v "SystemPaneSuggestionsEnabled" /t REG_DWORD /d 0 /f')
        except:
            pass

        Done()
        os._exit(0)
    if x != "" or x != " " or x != "y" or x != "Y" or x != "yes" or x != "Yes" or x != "YES":
        Done()
        os._exit(0)

# 📝 May close this
def gotoLight():
    print("[*] This program will:")
    print("[>] Set up a white mountain wallpaper (437 KB)")
    printLogInstallBasics()
    beginOrNah()
    os._exit(1)

# 📝 May close this
def gotoDark():
    print("[*] This program will:")
    print("[>] Set up a dark wallpaper (437 KB)")
    printLogInstallBasics()
    beginOrNah()
    Basics()
    os._exit(1)

# 🎈 Main menu
def main():
    print(Style.RESET_ALL)

    print(Fore.WHITE + "       A tool to set-up Windows 10 faster and easier")
    print("               Last updated " + Fore.CYAN + "2022 July 22")

    print(Style.RESET_ALL)

    if len(sys.argv) == 1:
        print("[x] Please run this program with args, or type 'py "  + sys.argv[0] + " help'")
        print(Style.RESET_ALL)
        os._exit(0)
    if len(sys.argv) == 2:
        print("[x] Please run this program with args, or type 'py "  + sys.argv[0] + " help'")
        print(Style.RESET_ALL)
        os._exit(0)

    if str(sys.argv[1]) == "help":
        print("There are 2 args for the first, 'light' and 'dark', you can choose which one u prefer")
        print("There are 2 more args for the second, 'winget' and 'requests', its how you want the files to be installed")
        print("To set up your machine for dark mode you would need to type 'py "  + sys.argv[0] + " dark [requests/winget]'")
        print("This wont be instant, no need for stress; you will be asked")
        print("ezWindows is also open-source, no obfuscation; incase you do not trust this.")
        print(Style.RESET_ALL)
        os._exit(1)

    if str(sys.argv[1]) == "whoami":
        print("                         " + username)
        print(Style.RESET_ALL)
        os._exit(1)

    if str(sys.argv[1]) != "light":
        if str(sys.argv[1]) != "dark":
            print("[x] Canceled, the valid arguments are 'light' or 'dark'")
            print("[?] Example: 'py "  + sys.argv[0] + " dark [requests/winget]' to set up this machine for dark mode")
            print(Style.RESET_ALL)
            os._exit(0)
    
    if str(sys.argv[2]) != "requests":
        if str(sys.argv[2]) != "winget":
            print("[x] Canceled, the valid arguments for the downloads are 'requests' or 'winget'")
            print("[?] Example: 'py "  + sys.argv[0] + " dark [requests/winget]' to set up this machine for dark mode")
            print(Style.RESET_ALL)
            os._exit(0)

    print("Setting up " + sys.argv[1] + " mode")

    print(Style.RESET_ALL)

    if str(sys.argv[1]) == "light":
        gotoLight()
        os._exit(0)
    gotoDark()
    os._exit(0)

# 🔧 If you are here to change code, this is the best thing u can change
main()
