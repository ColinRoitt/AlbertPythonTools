# -*- coding: utf-8 -*-

"""Search Google Fast."""

from albertv0 import *
import os

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Google Quicker"
__version__ = "1.0"
__trigger__ = "!g "
__author__ = "Colin Roitt"
__doc__ = "Search google faster directly from Albert"


baseurl = 'https://www.google.com/search?q='
iconPath = os.path.dirname(__file__)+"/google.svg"
    
def handleQuery(query):
    if not query.isTriggered:
        return
    
    stripped = query.string.strip()

    if not stripped:
        return    
    
    url = baseurl + stripped.replace(' ', '%20')

    return Item(id=__prettyname__,
                icon=iconPath,
                text="Search: " + stripped,
                subtext= 'Search with Google ' + url,
                actions=[
                    UrlAction("Search term on Google", url),
                    ClipAction("Copy URL", url)
                ])