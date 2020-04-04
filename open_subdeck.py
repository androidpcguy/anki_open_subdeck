# Copyright 2020 Akshara Balachandra <akshara.bala.18@gmail.com>
# License: GNU GPLv3; see included license file

import aqt
from aqt import mw

from aqt.qt import *

__version__ = "0.1"

config = mw.addonManager.getConfig(__name__)
shortcut_key = config['shortcut']

MENU_ITEM = "Browse current deck"

def launch_browser():

    curDid = None

    if(mw.reviewer.card):
        curDid = mw.reviewer.card.did
    else: # defaults to regular browse if not in reviewer
        mw.onBrowse()
        return

    curDeckName = mw.col.decks.name(curDid)

    searchText = 'deck:\"{}\"'.format(curDeckName)

    browser = aqt.dialogs.open("Browser", mw)
    browser.form.searchEdit.lineEdit().setText(searchText)
    browser.onSearchActivated()

browse = QAction(MENU_ITEM, mw)
browse.triggered.connect(launch_browser)

# set shortcut
browse.setShortcut(QKeySequence(shortcut_key))

# add menu item to "Tools" menu
mw.form.menuTools.addAction(browse)
