import subprocess
from subprocess import Popen, PIPE
import time

while True:
	# write your pathes instead of these
    subprocess.call(["C:/cygwin/bin/run.exe", "scp root@10.1.1.10:a.jpg C:/cygwin/home/Nelly/ZBar/bin/"])
    try:
        str = subprocess.check_output(["C:/cygwin/home/Nelly/ZBar/bin/zbarimg.exe","C:/cygwin/home/Nelly/ZBar/bin/a.jpg"])
        print str
	# write your car number instead of this
        if str.find("35-210-69")!= -1:
            print "yay!"
            exit(0)
    except subprocess.CalledProcessError:
        print "not your car...\n"
    time.sleep(2)        
