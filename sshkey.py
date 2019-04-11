import sys
import datetime
import subprocess
now = lambda: datetime.datetime.now().timestamp()
run = lambda cmd: subprocess.run(cmd, shell=True)
run('ssh-keygen -f indev_sshkey -t ecdsa -b 521')
