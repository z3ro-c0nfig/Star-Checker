import os, requests, time, random, string, datetime, json, msvcrt, sys
from wonderwords import RandomWord

########### Default Configuration ###########

default_config = {
    "version": "1.0",
    
    "configuration": {
        "webhook": {
            "enabled": None,
            "url": None
        },
        "proxy": {
            "enabled": None,
            "type": None,
            "filePath": None
        },
        "liteMode": {
            "enabled": None
        }
    },

    "lastOptions": {
        "default": {
            "generationMethod": None,
            "maximumCharacters": None,
            "minimumCharacters": None,
            "include": None,
            "startsWith": None,
            "endsWith": None,
            "mode": None,
            "proxy": None,
            "timeout": None
        },
        "platforms": {
            "socials": {
                "tiktok": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "instagram": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "snapchat": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "twitter": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                }
            },
            "entertainment": {
                "youtube": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "twitch": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "kick": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "discord": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                }
            },
            "gaming": {
                "steam": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "epicgames": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "xboxtag": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "minecraft": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "roblox": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "playstation": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "battlenet": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "riotgames": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                }
            },
            "other": {
                "domain": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "soundcloud": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "gmail": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                },
                "placeholder": {
                    "generationMethod": None,
                    "maximumCharacters": None,
                    "minimumCharacters": None,
                    "include": None,
                    "startsWith": None,
                    "endsWith": None,
                    "mode": None,
                    "proxy": None,
                    "timeout": None
                }
            }
        }
    }
}

########### Interface ###########

banner = """╔═══════════════════════════════════════════════════════════════╗
║ .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▄       ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄   ║
║ ▐█ ▀. •██  ▐█ ▀█ ▀▄ █·    ▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █· ║
║ ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▐▀▀▄     ██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄  ║
║ ▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█•█▌    ▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌ ║
║  ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀    ·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀ ║
╚═══════════════════════════════════════════════════════════════╝"""

main = """╔═══════════════════════════════════════════════════════════════╗
║ .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▄       ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄   ║
║ ▐█ ▀. •██  ▐█ ▀█ ▀▄ █·    ▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █· ║
║ ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▐▀▀▄     ██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄  ║
║ ▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█•█▌    ▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌ ║
║  ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀    ·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀ ║
╠═══════════════════════════Social══════════════════════════════╣
║ [01] TikTok  [02] Instagram   [03] Snapchat   [04] Twitter    ║
╠════════════════════════Entertainment══════════════════════════╣
║ [05] Youtube [06] Twitch      [07] Kick       [08] Discord    ║
╠═══════════════════════════Gaming══════════════════════════════╣
║ [09] Steam   [10] Epic Games  [11] Xbox Tag   [12] Minecraft  ║
║ [13] Roblox  [14] Playstation [15] Battle.net [16] Riot Games ║
╠════════════════════════════Other══════════════════════════════╣
║ [17] Domain  [18] SoundCloud  [19] Gmail      [20] Placholder ║
╠═══════════════════════════Config══════════════════════════════╣
║ [21] Webhook [22] Proxy Mode  [23] Lite Mode  [24] Exit       ║
╠═══════════════════════════════════════════════════════════════╣
║ Select option >                                               ║
╚═══════════════════════════════════════════════════════════════╝"""

checking = """╔═══════════════════════════════════════════════════════════════╗
║ .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▄       ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄   ║
║ ▐█ ▀. •██  ▐█ ▀█ ▀▄ █·    ▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █· ║
║ ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▐▀▀▄     ██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄  ║
║ ▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█•█▌    ▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌ ║
║  ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀    ·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀ ║
╠══════════════════════════Statistics═══════════════════════════╣
║                                                               ║
╠════════════════════════════Logs═══════════════════════════════╣
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝"""

logs = """╔═══════════════════════════════════════════════════════════════╗
║ .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▄       ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄   ║
║ ▐█ ▀. •██  ▐█ ▀█ ▀▄ █·    ▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █· ║
║ ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▐▀▀▄     ██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄  ║
║ ▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█•█▌    ▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌ ║
║  ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀    ·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀ ║
╠════════════════════════════Logs═══════════════════════════════╣
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝"""

modes = """╔═══════════════════════════════════════════════════════════════╗
║ .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▄       ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄   ║
║ ▐█ ▀. •██  ▐█ ▀█ ▀▄ █·    ▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █· ║
║ ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▐▀▀▄     ██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄  ║
║ ▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█•█▌    ▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌ ║
║  ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀    ·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀ ║
╠═══════════════════════════Options═════════════════════════════╣
║ [01] Generation Method: {GenerationMethodState}║
║ [02] Maximum Characters: {MaximumCharactersState}║
║ [03] Minimum Characters: {MinimumCharactersState}║
║ [04] Include: {IncludeState}║
║ [05] Starts With: {StartsWithState}║
║ [06] Ends With: {EndsWithState}║
║ [07] Mode: {ModeState}║
║ [08] Proxy: {ProxyState}║
╠═════════════════════════════Start═════════════════════════════╣
║                    Enter 0 to start checking                  ║
╚═══════════════════════════════════════════════════════════════╝"""

########### Modules ###########

def clr():
    os.system('cls')

########### Platforms - Social ###########

def TikTok():
    print("Running Option 1")

def Instagram():
    print("Running Option 2")

def Snapchat():
    print("Running Option 3")

def Twitter():
    print("Running Option 1")

########### Platforms - Entertainment ###########

def Youtube():
    print("Running Option 2")

def Twitch():
    print("Running Option 3")

def Kick():
    print("Running Option 1")

def Placeholder():
    print("Running Option 2")

########### Platforms - Gaming ###########

def Steam():
    print("Running Option 2")

def EpicGames():
    print("Running Option 3")

def XboxTag():
    print("Running Option 1")

def Minecraft():
    clr()
    print("")

def Roblox():
    print("Running Option 2")

def Playstation():
    print("Running Option 3")

def Battlenet():
    print("Running Option 1")

def RiotGames():
    print("Running Option 2")

########### Platforms - Other ###########

def Domain():
    print("Running Option 2")

def SoundCloud():
    print("Running Option 3")

def Gmail():
    print("Running Option 1")

def Placeholder():
    print("Running Option 2")

########### Config ###########

def Webhook():
    print("Running Option 2")

def ProxyMode():
    print("Running Option 3")

def LiteMode():
    print("Running Option 1")

def Exit():
    clr()
    print(banner)
    print("Bye bye <3")
    time.sleep(0.5)
    exit()

########### Get State ###########

def GetGernerationMethodState():
    pass

def GetMaximumCharactersState():
    return "Not Set"

def GetMinimumCharactersState():
    return "Not Set"

def GetIncludeState():
    return "Not Set"

def GetStartsWithState():
    return "Not Set"

def GetEndsWithState():
    return "Not Set"

def GetModeState():
    return "Not Set"

def GetProxyState(PlatformType, Platform):
    with open('config.json', 'r') as f:
        data = json.load(f)
    ProxyState = data['lastOptions']['platforms'][PlatformType][Platform]['proxy']
    if ProxyState is None:
        ProxyState = data['lastOptions']['default']['proxy']
    if ProxyState is True:
        return "Enabled"
    elif ProxyState is False:
        return "Disabled"
    else:
        return "Disabled"

########### Set State ###########

def SetGenerationMethod():
    print("Setting Generation Method...")

def SetMaximumCharacters():
    print("Setting Maximum Characters...")

def SetMinimumCharacters():
    print("Setting Minimum Characters...")

def SetInclude():
    print("Setting Include...")

def SetStartsWith():
    print("Setting Starts With...")

def SetEndsWith():
    print("Setting Ends With...")

def SetMode():
    print("Setting Mode...")

def ToggleProxy(PlatformType, Platform):
    ProxyState = GetProxyState(PlatformType, Platform)
    if ProxyState == "Enabled":
        ProxyState = "Disabled"
    elif ProxyState == "Disabled":
        ProxyState = "Enabled"
    else:
        ProxyState = "Disabled"
    
    ProxyBool = True if ProxyState == "Enabled" else False

    with open('config.json', 'r') as f:
        data = json.load(f)

    data['lastOptions']['platforms'][PlatformType][Platform]['proxy'] = ProxyBool
    data['lastOptions']['default']['proxy'] = ProxyBool

    with open('config.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    return ProxyState

def StartChecking():
    print("Starting")

OptionsMinecraft = {
    '1': SetGenerationMethod,
    '2': SetMaximumCharacters,
    '3': SetMinimumCharacters,
    '4': SetInclude,
    '5': SetStartsWith,
    '6': SetEndsWith,
    '7': SetMode,
    '8': lambda: ToggleProxy('gaming', 'minecraft'),
    '0': StartChecking,
}
    
########### Main ###########

menu = {
    # Social
    '1': TikTok,
    '2': Instagram,
    '3': Snapchat,
    '4': Twitter,
    # Entertainment
    '5': Youtube,
    '6': Twitch,
    '7': Kick,
    '8': Placeholder,
    # Gaming
    '9': Steam,
    '10': EpicGames,
    '11': XboxTag,
    '12': Minecraft,
    '13': Roblox,
    '14': Playstation,
    '15': Battlenet,
    '16': RiotGames,
    # Other
    '17': Domain,
    '18': SoundCloud,
    '19': Gmail,
    '20': Placeholder,
    # Config
    '21': Webhook,
    '22': ProxyMode,
    '23': LiteMode,
    '24': Exit,
}

def Main():
    clr()
    print(main)

    sys.stdout.write("\033[2A")
    sys.stdout.write("\033[18C")
    sys.stdout.flush()

    digits = ""

    while True:
        key = msvcrt.getch()

        if key in b"\r\n":
            break

        if key == b"\x08" and len(digits) > 0:
            digits = digits[:-1]
            sys.stdout.write("\b \b")
            sys.stdout.flush()
            continue

        if key.isdigit() and len(digits) < 2:
            digits += key.decode()
            sys.stdout.write(key.decode())
            sys.stdout.flush()

    sys.stdout.write("\033[2B\n")
    sys.stdout.flush()

    if digits in menu:
        menu[digits]()
    else:
        Main()

def Start():
    os.system('title ★ Star Checker && color 5')
    clr()
    print(banner)

    print("Loading config.json...")
    if os.path.exists('config.json'):
        with open('config.json', 'r') as f:
            data = json.load(f)
            print("Loaded config.json!")
    else:
        with open('config.json', 'w') as f:
            json.dump(default_config, f, indent=4)
            print("config.json created with default settings!")
        data = default_config

    print(f"Version: {data['version']}")
    print("Checking for new version")

    r = requests.get("https://pastebin.com/raw/1wPCFR91")
    if r.status_code == 200:
        if r.text == data['version']:
            print("Your on the latest version")
        else:
            print(f"New version availble! {data['version']} --> {r.text}")
    else:
        print("Error checking for new version")
    input("Press enter to continue...")
    Main()

if __name__ == "__main__": 
    Start()
