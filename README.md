# OSRS Mining Bot

A simple bot that will automate mining the 3-node iron ore spot in the Al Kharid mines in Old School Runescape. This project is a work in progress, I am planning on improving it by adding more scripts for other tasks in OSRS, as well as improvements to the image recognition algorithms used for more consistent performance. Use this script at your own risk, I added some randomness to the bot but I am not certain it is enough to evade Jagex's bot detection. 

### Install

* [Download and install Python3](https://www.python.org/downloads/)
* [Download and install pip](https://pypi.org/project/pip/)
* Open Command Prompt
* Navigate to the directory you would like to install `osrs-mining-bot` (i.e. `cd Documents` will navigate you to your Documents folder)
* Type `git clone https://github.com/FlimsyFuares/osrs-mining-bot.git`
* Enter the directory by typing `cd osrs-mining-bot`
* Download the Python libraries used by the bot by typing `pip install -r requirements.txt`
* Log into Runescape client and find the 3-node iron ore spot at the Al Kharid mines
* Return to the command prompt window, and type `python main.py "Window Name"`
    * Replace "Window Name" with the name of the window for your OSRS client.
    * RuneLite's window name is something like: `RuneLite - Username`
* The bot should now get to work mining for you, and will dump its inventory automatically so that you can leave it running with minimal supervision
    * To terminate the bot script, open the command prompt that the script is running in and press `Ctrl+C`

### Issues

* Please leave any feedback or issues in the Issues tab!

### Donate

This tool is completely free, but if you would like to support me, you can with Ethereum:

ETH: 0x363d9Eb6971B71ac57f2EeD4a615E5403eC72aDB