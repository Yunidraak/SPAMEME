# coding: utf-8

"""

v 1.0.0

SPAMEME is a program used to facilitate memes spam. This program
is currently only usable on windows with the Python PATH if you
have not previously installed the Python requests, pyperclip and
pyautogui libraries. It is currently usable to spam memes on
discord and whatsapp web, but only on 17-inch computers for the
latter. This program currently requires that your computer is not
used during the operation.

For more information about starting the program, use help(start).
For more information about Discord spam, use help(discord). For more
information about spam on Whatsapp Web, use help(whatsapp_web).

For more questions or comments, please use the API which is not yet
available because the developers are too lazy.

"""

import os, time, keyboard

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests

try:
    import pyperclip
except ModuleNotFoundError:
    os.system("pip install requests")
    import pyperclip

try:
    import pyautogui
except ModuleNotFoundError:
    os.system("pip install requests")
    import pyautogui


def discord(subreddit="", count=1):

    """
Help on added function discord in SPAMEME module:

discord(...)
    discord(subreddit="", count=1)
    
    Spam from memes on Discord.
    Optional keywords arguments:
    subreddit: The subreddit from which the memes will be
    extracted, default a random one.
    count: The number of memes that will be spammed, default one.
    Caution. For the proper functioning of spam, you must place
    your cursor in the writing bar of the conversation on which
    you want to spam the same. You must then press enter, and you
    will then have 5 seconds before the spam starts. Then you
    have to wait until the end of the spam to be able to resume
    other activities.
"""

    print("\nFor the proper functioning of spam, you must place your cursor in the writing bar of the\nconversation on which you want to spam the same. You must then press enter, and you will then have\n5 seconds before the spam starts. Then you have to wait until the end of the spam to be able to\nresume other activities.\n\nPress enter to continue.", end=" ")

    go = False

    while go == False:

        if keyboard.is_pressed("enter"):
            go = True
    
    time.sleep(5)

    if count == 1:
        operation = 0
    else:
        operation = 1

    if operation == 0:

        query = str("https://meme-api.herokuapp.com/gimme/" + str(subreddit))
        memedata = requests.get(query)
        memeinfo = memedata.json()
        memeurl = memeinfo["url"]
        pyperclip.copy(memeurl)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press("enter")

    else:

        number = str(count)
        query = str("https://meme-api.herokuapp.com/gimme/" + str(subreddit) +
                    str(number))
        memesdata = requests.get(query)
        memesinfo = memesdata.json()
        memes = memesinfo["memes"]

        for i in range(count):
            memeurl = memes[i]["url"]
            pyperclip.copy(memeurl)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(3)
            pyautogui.press("enter")


def whatsapp_web(subreddit="", count=1):

    """
Help on added function whatsapp_web in SPAMEME module:

whatsapp_web(...)
    whatsapp_web(subreddit="", count=1)
    
    Spam from memes on Whatsapp Web (internet browser).
    Optional keywords arguments:
    subreddit: The subreddit from which the memes will be
    extracted, default a random one.
    count: The number of memes that will be spammed, default one.
    Caution. For the proper functioning of spam, you need to open
    two tabs in your browser, open Whatsapp Web in the second one
    and place your cursor in the writing bar of the conversation
    you want to spam the same. You must then press enter, and you
    will then have 5 seconds before the spam starts. Then you
    have to wait until the end of the spam to be able to resume
    other activities.
"""

    print("\nFor the proper functioning of spam, you need to open two tabs in your browser, open Whatsapp Web\nin the second one and place your cursor in the writing bar of the conversation you want to spam\nthe same. You must then press enter, and you will then have 5 seconds before the spam starts.\nThen you have to wait until the end of the spam to be able to resume other activities.\n\nPress enter to continue.", end=" ")

    go = False

    while go == False:

        if keyboard.is_pressed("enter"):
            go = True

    time.sleep(5)

    if count == 1:
        operation = 0
    else:
        operation = 1

    if operation == 0:

        query = str("https://meme-api.herokuapp.com/gimme/" + str(subreddit))
        memedata = requests.get(query)
        memeinfo = memedata.json()
        memeurl = memeinfo["url"]
        pyperclip.copy(memeurl)
        pyautogui.click(x=115, y=20)
        time.sleep(1)
        pyautogui.click(x=340, y=50)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click(x=765, y=500, button="right")
        time.sleep(1)
        pyautogui.click(x=780, y=510)
        time.sleep(1)
        pyautogui.click(x=345, y=20)
        time.sleep(1)
        pyautogui.click(x=915, y=810)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)

    else:

        number = str(count)
        query = str("https://meme-api.herokuapp.com/gimme/" + str(subreddit) +
                    str(number))
        memesdata = requests.get(query)
        memesinfo = memesdata.json()
        memes = memesinfo["memes"]

        for i in range(count):
            memeurl = memes[i]["url"]
            pyperclip.copy(memeurl)
            pyautogui.click(x=115, y=20)
            time.sleep(1)
            pyautogui.click(x=340, y=50)
            time.sleep(1)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.click(x=765, y=500, button="right")
            time.sleep(1)
            pyautogui.click(x=780, y=510)
            time.sleep(1)
            pyautogui.click(x=345, y=20)
            time.sleep(1)
            pyautogui.click(x=915, y=810)
            time.sleep(1)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)


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
        "\n   #@@@@@@@@@@# #@@@@@@@@@@# #@@@@@@@@#  #@@@@@@@##@@@@@@@##@@@@@@@@@#@@@@@@@##@@@@@@@##@@@@@@@@@#\n  #@          @#@          @#@        @# @       @@       @@         @       @@       @@         @\n  @     @@    .@@     @     @@        .@ @       @/       @@     ....@       #@       @@     ....@\n  @.     @@@@@@#@     @,    @@    @    @ @       (        @@     @@@@@        %       @@     @@@@#\n  #@,       /@@#@          ,@.    @    @#@    #           @@         @           /    @@         @\n   #@@@%      .@@        *@@@    .@     @@    %     *     @@     ____@     .     (    @@     ____@\n  @/    @@     @@     @@@@##@           @@    %.    @     @@     @@@@@     @    .(    @@     @@@@#\n  @&    &@     @@     @    @,    ,@.    #@    %@    @     @@         @     @    @#    @@         @\n   @@        .@#@     @    @     &@@     @    %@   *@     @@         @     @*   @#    @@         @\n    #@@@@@@@@@# #@@@@@#    #@@@@@@ #@@@@@@@@@@@#@@@@#@@@@@##@@@@@@@@@#@@@@@#@@@@#@@@@@##@@@@@@@@@#\n                                                                                           v 1.0.0\n  ╔═════════════════════════════════════════════════════════════════╗\n  ║                                                                 ║     ONE DOES NOT SIMPLY      \n  ║   Licensed under the MIT License                                ║         _-----_              \n  ║   Copyright (c) 2021 Yunidraak                                  ║        /___.-\ \             \n  ║                                                                 ║       ||__ _\_\ \            \n  ║   If any problem with the program, type help() in the Python    ║       |\ #. *  \ )           \n  ║   terminal after this program finished to run and then type     ║    _-┬n¬\  ==¯ ) )--__       \n  ║   SPAMEME.                                                      ║   / /¯()\¯\@@#¯_-¯¯_/ ¯¯--   \n  ║   For more questions or comments, please use the API which is   ║   |\   /     \  |¯           \n  ║   not yet available because the developers are too lazy.        ║   /¯¯¯¯|      | |            \n  ║                                                                 ║    SPAM MEMES WITH PYTHON    \n  ╚═════════════════════════════════════════════════════════════════╝"
    )

    time.sleep(1)

    print(
        "\n\nDo you want to choose a special subreddit from which the memes will be extracted [Y/n]?",
        end=" ")

    choice = False

    while choice == False:

        if keyboard.is_pressed("Y") or keyboard.is_pressed("y"):
            choice = "y"

        elif keyboard.is_pressed("N") or keyboard.is_pressed("n"):
            choice = "n"

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
                    "\nInternet isn't available. Please reconnect to continue."
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

    option = False

    print("\nDo you want to spam the memes on Discord or Whatsapp Web [d/w]?",
          end=" ")

    while option == False:

        if keyboard.is_pressed("D") or keyboard.is_pressed("d"):
            option = "discord"
            print("\n")

        if keyboard.is_pressed("W") or keyboard.is_pressed("w"):
            option = "whatsapp_web"
            print("\n")
    
    if option == "discord":
        discord(subreddit, count)
    elif option == "whatsapp_web":
        whatsapp_web(subreddit, count)
    else:
        pass


