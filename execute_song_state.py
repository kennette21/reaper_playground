import requests

def get_song_state():
    resp = requests.get('http://127.0.0.1:5000/')
    song_state = eval(resp.content)
    return song_state

def execute_song_state(song_state):
    for idx, mute_value in enumerate(song_state):
        track = RPR_GetTrack(0,idx)
        RPR_SetMediaTrackInfo_Value(track, 'B_MUTE', not bool(mute_value))

def get_and_execute():
    song_state = get_song_state()
    execute_song_state(song_state)

RPR_defer("get_and_execute()")
