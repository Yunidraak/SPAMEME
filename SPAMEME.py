# coding: utf-8

"""

v 6.9

SPAMEME is a program used to facilitate memes spam. This program is currently
only usable on Windows with the Python PATH if you have not previously installed
the Python requests, win32clipboard, PIL, pyperclip and pyautogui libraries.
It is currently usable to spam memes as urls or pictures.
This program currently requires that your computer is not used during the spam.

For more information about starting the program, use help(start). For more
information about spam, use help(spam).

For more questions or comments, please use the API which is not yet available
because the developers are too lazy.

"""

import os, time, keyboard, sys, urllib.request
from io import BytesIO

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests

try:
    import win32clipboard
except ModuleNotFoundError:
    os.system("pip install pywin32")
    import win32clipboard

try:
    from PIL import Image
except ModuleNotFoundError:
    os.system("pip install Pillow")
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
Enter, and you will then have 5 seconds before the spam starts. Then you have to
wait until the end of the spam to be able to resume other activities.
  
Press enter to continue.""", end=" ")

    while not keyboard.is_pressed("enter"):
        pass

    time.sleep(5)

    memes = gimmemes(subreddit, count)

    print("\n\nSpamming memes                     ")

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
            memeurl = memes[i]["url"]
            pyperclip.copy(memeurl)

            pyautogui.hotkey("ctrl", "v")
            time.sleep(2)
            pyautogui.press("enter")


def gimmemes(subreddit="", count=1):

    """
Help on added function gimmemes in SPAMEME module:

gimmemes(...)
    gimmemes(subreddit="", count=1)

    Give the url(s) of meme(s), using meme-api.com.
    Optional keywords arguments:
    subreddit: The subreddit from which the memes will be
    given, default a random one.
    count: The number of memes that will be given, default one.
"""

    number = str(count)
    
    query = str("https://meme-api.com/gimme/"
    + str(subreddit) + number)
    memesdata = requests.get(query)
    memesinfo = memesdata.json()
    memes = memesinfo["memes"]
        

    if len(memes) != count:
            
        print("""

This operation can take a little moment.
Please wait.
""")
        d = count - len(memes)
        t = 0
        
        while d > 0 and t < 10 :
            
            query = str("https://meme-api.com/gimme/"
            + str(subreddit) + "50")
            memedata = requests.get(query)
            memeinfo = memedata.json()
            memeurls = memeinfo["memes"]
            
            
            i = 0
            l = len(memes)
            
            while d > 0 and i < 50 :
                
                j = 0
                
                while j < l and memes[j]["url"] != memeurls[i]["url"] :
                    j += 1
                    
                if j == l :
                    
                    memes.append(memeurls[i])
                    d -= 1
                    t = 0

                    print(str(d)
                    + " memes to copy remaining... ", end = "\r")
                    
                i += 1

            t += 1

        if d > 0:
            print("\n\nSorry, we did not find enough memes found to satisfy "
                  + "your request.\nHence the number of spammed memes will be"
                  , count - d, end = ".\r")

    return memes


def start(first=True):

    """
Help on added function start in SPAMEME module:

start(...)
    start(first=True)

    Function that runs when SPAMEME is launched.
    If first is set to True also prints the welcome message.
    It lasts from the moment you launch the program until the
    end, launching a different spam according to your choices.
    You can provide a subreddit (if you don't provide a subreddit
    or the provided subreddit doesn't exist, a random subreddit
    will be chosen), you must provide a number of memes to spam,
    and wether to spam the memes as urls or pictures.
"""

    if (first) :
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
                                                                           v 6.9
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
""", end = ""
        )

    time.sleep(1)

    print()

    choice = ""

    while choice == "":

        choice = input(
            "\nDo you want to choose the memes' subreddit source [Y/n]? ")

        if choice == "Y" or choice == "y" or choice == "" :
            choice = "y"

        elif choice == "N" or choice == "n":
            choice = "n"

        else:
            print(choice, "is not an option.")
            choice = ""

    subreddit = False

    while subreddit == False:

        if choice == "y":
            subreddit = input(
                "\nFrom which subreddit do you want the memes?\n> ") + "/"

            try:
                if len(subreddit) > 3 and subreddit[:2] == "r/":
                    subreddit = subreddit[2:]
                query = str("https://meme-api.com/gimme/" +
                            subreddit + "1")
                memetest = requests.get(query)
                memesinfo = memetest.json()
                memes = memesinfo["memes"]

            except:
                print(
                    "\nThe memes are out of reach, it can be because of one of"
                    + " the followings:\n\t- You are out of connection\n\t- "
                    + "The subreddit's name isn't valid\n\t- The subreddit "
                    + "doesn't exist anymore\nPlease check your connection and "
                    + "your input."
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
                    "\nThe amount of meme must be an integer superior or equal "
                    + "to 1."
                )
                count = False

        except:
            print(
                "\nThe amount of meme must be an integer superior or equal to 1."
            )
            count = False

    option = ""

    while option == "":

        option = input(
            "\nDo you want to spam the memes as urls or pictures [U/p]? ")

        if option == "U" or option == "u" or option == "":
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
        return

    
    time.sleep(1)
    restart = print("\n\nMission Accomplished.\nPress Enter to close the program"
                    + ", or press Space else to spam again.", end = " ")

    while not keyboard.is_pressed("enter"):
        if keyboard.is_pressed("space"):
            start(False)

start()
