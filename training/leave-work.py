# vars = ENG, PHL, CPS, ITC, TIME
# check time
# if time == ENG
# 

import sched
import time
import webbrowser

scheduler = sched.scheduler(time.time, time.sleep)

def sendme_toclass(url):
    webbrowser.open()

scheduler.enter(2, 1, sendme_toclass, ('http://sd.keepcalm-o-matic.co.uk/i/keep-calm-and-go-to-class-2.png'))
scheduler.enter(3, 1, sendme_toclass, ('http://sd.keepcalm-o-matic.co.uk/i/keep-calm-and-go-to-class-2.png'))

scheduler.run()