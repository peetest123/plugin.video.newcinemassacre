# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/FULLYCHARGEDSHOW
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.cinemassacre'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
YOUTUBE_CHANNEL_ID_1 = "JamesNintendoNerd"
YOUTUBE_CHANNEL_ID_2 = "Cinemassacre"
YOUTUBE_CHANNEL_ID_3 = "PL2B009153AC977F90"

# Entry point
def run():
    plugintools.log("FULLYCHARGEDSHOW.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("FULLYCHARGEDSHOW.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Cinemassacre Channel",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://dl.dropboxusercontent.com/u/50103581/avgn%20addon/latest%20videos.png",
        folder=True )
 
plugintools.add_item( 
        #action="", 
        title="Mikes Live Streams",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://dl.dropboxusercontent.com/u/50103581/avgn%20addon/mike.png",
        folder=True )
  
plugintools.add_item( 
        #action="", 
        title="Angry video game nerd episodes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://dl.dropboxusercontent.com/u/50103581/avgn%20addon/angry2.png",
        folder=True )
		

run()
