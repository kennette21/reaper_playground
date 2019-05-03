from reaper_python import *
import pyzbar.pyzbar as pyzbar
import sys
sys.path.insert(1,'/usr/local/lib/python2.7/site-packages')
import cv2

def msg(msg):
    RPR_ShowConsoleMsg(msg)
    return

msg("cv2 file: ")
msg(cv2.__file__)
msg("vers: ")
msg(cv2.__version__)


def async_stuff():
    try:
        # this process is running forever! why? how to find out
        # ret, frame = cap.read()
        # key = cv2.waitKey(0) & 0xFF
        # if key == ord("q"):
        #     return
        msg("is grabbed?: ")
        msg(cap.grab())
        ret, frame = cap.retrieve()
        msg("retrieved?: ")
        msg(ret)
    except cv2.error as e:
        msg("fucked up with this error: ")
        msg(e)
        msg(sys.exc_info()[0])

    # somethign is wrong here. with the read.
    # ret, frame = cap.read()
    # if ret:
    #     msg("got something!")
    # qr_codes = pyzbar.decode(frame)
    # qr_codes = [1]
    #
    # for code in qr_codes:
    #     msg(code.data)


    if str(RPR_GetProjExtState(0, "DummyToggleAction", "toggle_state", "", 123123)[4]) == "1":
        RPR_defer("async_stuff()")
    else:
        cap.release()


def main():
    async_stuff()

cap = cv2.VideoCapture(0)
main()
