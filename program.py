



import subprocess, sys
import Tkinter
import tkMessageBox


normal = "C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE"
debug_messages = False


location_this_is_running = sys.argv[0].replace("\\","/")

if len(sys.argv[1:]):
	filepath = sys.argv[1].replace("\\", "/")
	title = "RUNNING FOR REAL"
else:
	filepath = "NONE SPECIFIED"
	filepath = "C:\\Users\\ismdev\\Desktop\\test doc - Copy.rtf"
	title = "RUNNING TEST"

if debug_messages:
	tkMessageBox.showinfo(
		title,
		"RUNNING FROM {}\nOPENING {}\nWITH {}".format(
			location_this_is_running,
			filepath,
			normal
		)
	)

p = subprocess.Popen([
	normal,
	filepath
])
returncode = p.wait()

if debug_messages:
	tkMessageBox.showinfo(
		title,
		"RETURN CODE WAS {}"
		.format(returncode)
	)