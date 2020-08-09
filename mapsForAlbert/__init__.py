# -*- coding: utf-8 -*-

"""Search Google Maps Fast."""

from albertv0 import *
import os

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Maps Quicker"
__version__ = "1.0"
__trigger__ = "!m "
__author__ = "Colin Roitt"
__doc__ = "Search google maps faster directly from Albert"


baseurl = 'https://www.google.co.uk/maps/search/'
iconPath = os.path.dirname(__file__)+"/maps.svg"
    
def handleQuery(query):
    if not query.isTriggered:
        return
    
    stripped = query.string.strip()

    if not stripped:
        return    
    
    url = baseurl + stripped.replace(' ', '+')

    return Item(id=__prettyname__,
                icon=iconPath,
                text="Search: " + stripped,
                subtext= 'Search with Maps ' + url,
                actions=[
                    UrlAction("Search term on Google Maps", url),
                    ClipAction("Copy URL", url)
                ])
