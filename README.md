# AttachScript
Skeleton for creating an EXE that files are launched by that runs a script before it fully launches.

## Instructions
* (Stub for creating link to custom script).
* Open config.py and set `replacing` to the path of the default program you are replacing.
* Select an icon that you want the files to look like.
* Open up **build_exe.bat** and change `--icon=icon.ico` to `--icon=PATH TO YOUR ICON.ico`.
* Run build_exe.bat.
* Navigate to the new /dist directory.
* Rename program.exe to the program of your choosing.
* Find a program that uses the default program you are replacing.
* Change its default program to this new program in the /dist directory.

#### Notes
To get the icon of something, say for OFFICE, this is useful.
https://superuser.com/questions/964417/ms-office-file-types-icon-dll-location