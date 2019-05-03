def toggle_mute(track):
    if RPR_GetMediaTrackInfo_Value(track, 'B_MUTE'):   
      RPR_SetMediaTrackInfo_Value(track, 'B_MUTE', False)
    else:
      RPR_SetMediaTrackInfo_Value(track, 'B_MUTE', True)
        
toggle_mute(RPR_GetTrack(0,2))
