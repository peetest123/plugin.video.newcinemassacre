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
YOUTUBE_CHANNEL_ID_4 = "PLbQ-gSLYQEc7NPEexZVMKfvDJinOsL7YF"
YOUTUBE_CHANNEL_ID_5 = "PLbQ-gSLYQEc4Ah-5yF3IH29er13oJs_Xy"
YOUTUBE_CHANNEL_ID_6 = "PLb8K22b6dc0xc8K2VHDGj7LeNLdbPEbN_"
YOUTUBE_CHANNEL_ID_7 = "PLb8K22b6dc0xuu7OXxc6MYRtaZ7AQxveW"
YOUTUBE_CHANNEL_ID_8 = "PLb8K22b6dc0z3w9sXD2-aTlapcK0odEZ2"
YOUTUBE_CHANNEL_ID_9 = "PLb8K22b6dc0wo6jhgOnIVeAXgAKXgAM4l"

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
        title="The Latest Videos",
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

plugintools.add_item( 
        #action="", 
        title="Board James",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://dl.dropboxusercontent.com/u/50103581/avgn%20addon/bj.png",
        folder=True )

plugintools.add_item( 
        #action="", 
        title="You Know Whats Bullshit ?",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://dl.dropboxusercontent.com/u/50103581/avgn%20addon/bullshit.png",
        folder=True )
plugintools.add_item( 
        #action="", 
        title="Behind The Scenes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://dl.dropboxusercontent.com/u/50103581/avgn%20addon/bts.png",
        folder=True )
plugintools.add_item( 
        #action="", 
        title="Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://dl.dropboxusercontent.com/u/50103581/avgn%20addon/movies.png",
        folder=True )
plugintools.add_item( 
        #action="", 
        title="Reviews",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://dl.dropboxusercontent.com/u/50103581/avgn%20addon/reviews.png",
        folder=True )
plugintools.add_item( 
        #action="", 
        title="Extra Shit :)",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://dl.dropboxusercontent.com/u/50103581/avgn%20addon/extra.png",
        folder=True )
		
		
		
		

run()


