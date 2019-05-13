import requests
import pyzbar.pyzbar as pyzbar
from PIL import Image
from StringIO import StringIO
import sys
sys.path.insert(1,'/usr/local/lib/python2.7/site-packages')
import cv2


LOOP_TYPES = ["bass", "melody", "drum", "vocal"]
CUR_PLAYING = []
CONT_PLAYING = []
SOUNDS = {}
TYPE_CANNEL_MAPPER = {"bass": 0, "drum": 1, "vocal": 2, "melody": 3}
TRACK_DICT = {"bass": [], "drum": [], "vocal": [], "melody": []}

def detect_loop(image):
  qr_codes = pyzbar.decode(image)

  for code in qr_codes:
    loop = code.data
    # play/continue loop
    if loop in CUR_PLAYING:
      continue_loop(loop)
    else:
      loop_type = code.data.split("-")[0]
      if loop_type in LOOP_TYPES:
        start_loop(loop)

  manage_song()

def manage_song():
  for loop in CUR_PLAYING:
    if loop not in CONT_PLAYING:
      stop_loop(loop)


def start_loop(loop):
  msg("starting to play: " + loop)
  CUR_PLAYING.append(loop)
  CONT_PLAYING.append(loop)
  loop_type = loop.split("-")[0]
  index = int(loop.split("-")[1])
  toggle_mute(TRACK_DICT[loop_type][index])

def continue_loop(loop):
  # msg("continue playing: " + loop)
  CONT_PLAYING.append(loop)

def stop_loop(loop):
  msg("STOP PLAYING: " + loop)
  loop_type = loop.split("-")[0]
  index = int(loop.split("-")[1])
  try:
    msg("tryna stop")
    CUR_PLAYING.remove(loop)
    toggle_mute(TRACK_DICT[loop_type][index])
  except ValueError:
    msg("SHIT!! REMOVING ALREADY REMOVED SONG")

def toggle_mute(track):
    if RPR_GetMediaTrackInfo_Value(track, 'B_MUTE'):
      RPR_SetMediaTrackInfo_Value(track, 'B_MUTE', False)
    else:
      RPR_SetMediaTrackInfo_Value(track, 'B_MUTE', True)

def see_song():
    del CONT_PLAYING[:]
    # ret, pl_img = cap.read()
    cur_img = requests.get("http://192.168.0.12:8080/shot.jpg")
    pl_img = Image.open(StringIO(cur_img.content))
    detect_loop(pl_img)
    toggle_state = str(RPR_GetProjExtState(0, "DummyToggleAction", "toggle_state", "", 123123)[4])
    if toggle_state == "1":
      RPR_defer("see_song()")

def msg(msg):
    RPR_ShowConsoleMsg(msg)
    RPR_ShowConsoleMsg("\n")
    return

def main():
    msg("wholly shit we started!!")

    for i in range(0,13):
        if (0 <= i <= 3):
            TRACK_DICT["bass"].append(RPR_GetTrack(0,i))
        elif (4 <= i <= 7):
            TRACK_DICT["drum"].append(RPR_GetTrack(0,i))
        elif (9 <= i <= 12):
            TRACK_DICT["melody"].append(RPR_GetTrack(0,i))

    msg("wholly shit we started!!")
    see_song()

# cap = cv2.VideoCapture(1)
main()
