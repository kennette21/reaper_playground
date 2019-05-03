import sys

def msg(msg):
    RPR_ShowConsoleMsg(msg)
    RPR_ShowConsoleMsg("\n")
    return

msg(sys.path)
msg("new path")
sys.path.insert(1,'/usr/local/lib/python2.7/site-packages')
msg(sys.path)

import cv2
msg(cv2.__file__)


#cap = cv2.VideoCapture(0)
#cap.release()
#cv2.destroyAllWindows()
