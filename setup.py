#!/usr/bin/python
#-*- encoding: utf-8 -*-
import os,time
code=open("usb.py","a")
def write(text):
    if text=="end":
        code.close()
        print "Code completed."
        print "You can run it by writing 'sudo python usb.py'"
        time.sleep(1)
        exit()
    code.write("\n%s" %(text))
write("""#!/usr/bin/python
#-*- encoding:utf-8 -*-
import os,time
os.system("pmset sleepnow")
time.sleep(1)
while True:""")
serial=raw_input("Serial Number of your USB device\n(You can get this by using 'system_profiler SPUSBDataType' in your terminal)\n:")
write("""    if "%s" in os.popen("system_profiler SPUSBDataType").read():
        break""" %(serial))
write("""os.system("caffeinate -u -t 1")""")
pswd=raw_input("Password of your Computer:")
write('''os.system(""" osascript -e 'tell application "System Events" to keystroke "%s"' """)''' %(pswd))
write('''os.system(""" osascript -e 'tell application "System Events"
	key code 76
end tell' """)''')
write("end")
