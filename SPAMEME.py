# coding: utf-8

"""

v 1.0.1

SPAMEME is a program used to facilitate memes spam. This program is currently
only usable on windows with the Python PATH if you have not previously installed
the Python requests, pyperclip and pyautogui libraries. It is currently usable
to spam memes as urls or pictures.
This program currently requires that your computer is not used during the spam.

For more information about starting the program, use help(start). For more
information about spam, use help(spam).

For more questions or comments, please use the API which is not yet available
because the developers are too lazy.

"""

import os, time, keyboard, sys, urllib.request
from io import BytesIO
import win32clipboard

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests

try:
    from PIL import Image
except ModuleNotFoundError:
    os.system("pip install PIL")
    from PIL import Image

try:
    import pyperclip
except ModuleNotFoundError:
    os.system("pip install pyperclip")
    import pyperclip

try:
    import pyautogui
except ModuleNotFoundError:
    os.system("pip install pyautogui")
    import pyautogui


def spam(subreddit="", count=1, output=0):

    """
Help on added function spam in SPAMEME module:

spam(...)
    spam(subreddit="", count=1, output=0)

    Spam from memes as urls or pictures.
    Optional keywords arguments:
    subreddit: The subreddit from which the memes will be extracted,
    default a random one.
    count: The number of memes that will be spammed, default one.
    output: The format of the output.
    1 stands for pictures, anything else for urls, default zero.
    Caution. For the proper functioning of spam, you must place
    your cursor in the writing bar of the conversation on which
    you want to spam the same. You must then press enter, and you
    will then have 5 seconds before the spam starts. Then you
    have to wait until the end of the spam to be able to resume
    other activities.
"""

    print(
        """
For the proper functioning of spam, you must place your cursor in the writing
bar of the conversation on which you want to spam the same. You must then press
enter, and you will then have 5 seconds before the spam starts. Then you have to
wait until the end of the spam to be able to resume other activities.
  
Press enter to continue.""", end=" ")

    go = False

    while go == False:

        if keyboard.is_pressed("enter"):
            go = True

    time.sleep(5)

    memes = gimmemes(subreddit, count)

    if output == 1:

        for i in range(count):
            memeurl = memes[i]
            urllib.request.urlretrieve(memeurl,
                "C:/Users/" + str(os.getlogin()) + "/Downloads/SPAMEMEtemp.png")

            image = Image.open("C:/Users/" + str(os.getlogin()) +
                        "/Downloads/SPAMEMEtemp.png")

            output = BytesIO()
            image.convert("RGB").save(output, "BMP")
            data = output.getvalue()[14:]
            output.close()

            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
            win32clipboard.CloseClipboard()

            pyautogui.hotkey("ctrl", "v")
            time.sleep(2)
            pyautogui.press("enter")

    else:
        for i in range(count):
            memeurl = memes[i]
            pyperclip.copy(memeurl)

            pyautogui.hotkey("ctrl", "v")
            time.sleep(2)
            pyautogui.press("enter")

    input("\n\nMission Accomplished.\nPress Enter to close the programm.")


def gimmemes(subreddit="", count=1):

    """
Help on added function gimmemes in SPAMEME module:

gimmemes(...)
    gimmemes(subreddit="", count=1)

    Give the url(s) of meme(s).
    Optional keywords arguments:
    subreddit: The subreddit from which the memes will be
    given, default a random one.
    count: The number of memes that will be given, default one.
"""

    if count == 1:
        operation = 0
    else:
        operation = 1

    if operation == 0:

        query = str("https://meme-api.herokuapp.com/gimme/" + str(subreddit))
        memedata = requests.get(query)
        memeinfo = memedata.json()
        memes = []
        memes.append(memeinfo["url"])

        return memes

    else:

        try:

            number = str(count)
            query = str("https://meme-api.herokuapp.com/gimme/"
            + str(subreddit) + "/" + str(number))
            memesdata = requests.get(query)
            memesinfo = memesdata.json()
            memes = memesinfo["memes"]

            if len(memes) != count:
                print("""
This operation can take a little moment.
Please wait.
""")
                memesinfo["morememes"]

            for i in range(len(memes)):
                memes[i] = memes[i]["url"]

        except KeyError:

            try:

                go = False

                memes = []

                while go == False:

                    query = str("https://meme-api.herokuapp.com/gimme/"
                    + str(subreddit) + "50")
                    memedata = requests.get(query)
                    memeinfo = memedata.json()
                    memeurls = memeinfo["memes"]
                    
                    for i in range(len(memeurls)):
                        
                        if memeurls[i]["url"] in memes or len(memes) == count:
                            pass
                        else:
                            memes.append(memeurls[i]["url"])
                            print(str(count-len(memes))
                            + " memes to copy remaining ", end="\r")

                        if len(memes) == count:
                            go = True

            except KeyError:

                try:

                    go = False

                    memes = []

                    while go == False:

                        query = str("https://meme-api.herokuapp.com/gimme/"
                        + str(subreddit))
                        memedata = requests.get(query)
                        memeinfo = memedata.json()
                        memeurls = memeinfo["url"]
                            
                        if memeurls["url"] in memes or len(memes) == count:
                            pass

                        else:
                            memes.append(memeurls["url"])
                            print(str(count-len(memes))
                            + " memes to copy remaining ", end="\r\r")

                        if len(memes) == count:
                            go = True

                except KeyError:

                    try:

                        print("""
Sorry, but it seems that this reddit doesn't exist.
Hence, the memes will be taken from a random reddit.""")

                        number = str(count)
                        
                        query = str("https://meme-api.herokuapp.com/gimme/" +
                                    str(number))
                        memesdata = requests.get(query)
                        memesinfo = memesdata.json()
                        memes = memesinfo["memes"]

                        for i in range(count):
                            memes[i] = memes[i]["url"]

                    except:

                        print("""
Sorry, but it seems that you doesn't have internet connection.
Please establish an internet connection.""")

        return memes


def start():

    """
Help on added function start in SPAMEME module:

start()

    Function that runs when SPAMEME is launched.
    It lasts from the moment you launch the program until the
    end, launching a different spam according to your choices.
    You can provide a subreddit (if you don't provide a subreddit
    or the provided subreddit doesn't exist, a random subreddit
    will be chosen), you must provide a number of memes to spam,
    and an application to spam on.
"""

    print(
        """
.#@@@@@@@@##@@@@@@@@@#;#@@@@@@@#;#@@@@@#;#@@@@@#@@@@@@@@#@@@@@#;#@@@@@#@@@@@@@@#
#/'      '\@.        \@@/     \@#@    '@#@'    @.       @    '@#@'    @.       @
@    ##    @.    .    @@       @#@     \@/     @.    ###@     \@/     @.    ###@
@    '@@@@@@.    @    @#   .   #@@      #      @.    ***@      #      @.    ***@
@\.      '\@.        /@*   #   *@@   )     (   @.    ;;;@   )     (   @.    ;;;@
#@@@@@,    @.    @@@@@@    @    @@   ).   .(   @.    @@@@   ).   .(   @.    @@@@
@    ##    @.    @# #@/         \@   #\   /#   @.    ###@   #\   /#   @.    ###@
@\.      ./@.    @# #@    #@#    @   @#   #@   @.       @   @#   #@   @.       @
'#@@@@@@@@@#@@@@@#; ;#@@@@@@@@@@@#@@@#@@@@@#@@@#@@@@@@@@#@@@#@@@@@#@@@#@@@@@@@@#
                                                                         v 1.0.1
╔═════════════════════════════════════════════════════╗                         
║ Licensed under the MIT License                      ║   ONE DOES NOT SIMPLY   
║ Copyright (c) 2021 Yunidraak                        ║         _-----_         
║                                                     ║        /___.-\ \        
║ If any problem with the program, type help() in the ║       ||__ _\_\ \       
║ Python terminal after this program finished to run  ║       |\ #. *  \ )      
║ and then type SPAMEME.                              ║   _-┬n¬\  ==¯ ) )--__   
║ For more questions or comments, please use the API  ║  / /¯()\¯\@@#¯_-¯¯_/ ¯¯-
║ which is not yet available because the developers   ║  |\   /     \  |¯       
║ are too lazy.                                       ║ /¯¯¯¯|      | |         
╚═════════════════════════════════════════════════════╝  SPAM MEMES WITH PYTHON 
"""
    )

    time.sleep(1)

    print("\n\n")

    choice = ""

    while choice == "":

        choice = input(
            """Do you want to choose the subreddit from which the memes will be extracted?
[Y/n]? """)

        if choice == "Y" or choice == "y":
            choice = "y"

        elif choice == "N" or choice == "n":
            choice = "n"

        else:
            print(choice, "is not an option.")
            choice = ""

    print()

    subreddit = False

    while subreddit == False:

        if choice == "y":
            subreddit = input(
                "\nFrom which subreddit do you want the memes?\n> ")

            try:
                query = str("https://meme-api.herokuapp.com/gimme/" +
                            str(subreddit))
                memetest = requests.get(query)

            except:
                print(
                    "\nThe subredit's name isn't valid or doesn't exist anymore.\nPlease verify your input."
                )
                subreddit = False

        elif choice == "n":
            subreddit = ""

    count = False

    while count == False:

        try:

            count = int(input("\nWhich amount of memes do you want?\n> "))

            if count < 1:
                print(
                    "\nThe amount of meme must be an integer superior or equal to 1."
                )
                count = False

        except:
            print(
                "\nThe amount of meme must be an integer superior or equal to 1."
            )
            count = False

    option = ""

    print()

    while option == "":

        option = input(
            "\nDo you want to spam the memes as url or pictures [u/p]? ")

        if option == "U" or option == "u":
            option = "url"

        elif option == "P" or option == "p":
            option = "picture"

        else:
            print(option, "is not an option.")
            option = ""

    if option == "url":
        spam(subreddit, count, 0)
    elif option == "picture":
        spam(subreddit, count, 1)
    else:
        pass

start()
