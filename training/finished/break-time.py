import time
import webbrowser
import tkMessageBox
import Tkinter


window = Tkinter.Tk()
localtime = time.localtime(time.time())

while True:

	window.wm_withdraw()
	tkMessageBox.showinfo(title="break time", message="Hi, Marcus. Time for a break!")
	webbrowser.open("http://www.youtube.com/watch?v=ddtfoiaWGqs")

	time.sleep(3600)

# check the time 
# if the time has passed
# sleep for an hour
