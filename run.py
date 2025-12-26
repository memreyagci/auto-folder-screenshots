import os
import win32gui
from mss import mss
from datetime import datetime
from win11toast import toast

curr_date = datetime.now()
curr_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())

desired_window = "AWS Certified Cloud Practitioner Certification Course (CLF-C02) - Pass the Exam! - YouTube - Brave"

save_dir = os.environ['USERPROFILE'] + '\\Desktop\\AWS Practice\\'
ss_file_name = f"Screenshot {curr_date.year}-{curr_date.month}-{curr_date.day} {curr_date.hour:02}{curr_date.minute:02}{curr_date.second:02}.png"

if(curr_window == desired_window):
    with mss() as sct:
        sct.shot(output = save_dir+ss_file_name)
    toast("AutoFolderScreenshots", "Saved to " + save_dir)
else:
    os.system('start explorer.exe ms-screenclip:')
