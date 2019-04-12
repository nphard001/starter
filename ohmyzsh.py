import os
import sys
import hashlib
import tempfile
import datetime
import subprocess
md5 = lambda x: hashlib.md5(x.encode('utf-8')).hexdigest()
now = lambda: datetime.datetime.now().timestamp()
def run(cmd):
    print('[run]', cmd, file=sys.stderr)
    return subprocess.run(cmd, shell=True).returncode

run(f'sudo apt-get install -y zsh')
run(f'sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"')
