

"""
program.py

Description of file

@author: namx-holi
@date:   2018-02-16
"""

import config
import os
import subprocess
import sys

import Tkinter
import tkMessageBox


location_this_is_running = sys.argv[0].replace("\\","/")

debug_messages = False


def run_script(script_path):

	proc = subprocess.Popen(
		script_path,
		creationflags=subprocess.SW_HIDE,
		shell=True
	)


if len(sys.argv[1:]):
	filepath = sys.argv[1].replace("\\", "/")
	title = "RUNNING FOR REAL"

else:
	filepath = "NONE SPECIFIED"
	filepath = "C:\\Users\\ismdev\\Desktop\\test doc - Copy.rtf"
	title = "RUNNING TEST"


run_script(config.on_startup)


p = subprocess.Popen([
	config.replacing,
	filepath
])

returncode = p.wait()

run_script(config.on_closing)