import os
import sys
import json
import datetime
import subprocess

report = []


def now():
    return datetime.datetime.now().timestamp()


def run(cmd):
    global report
    st = now()
    print('[run]', cmd, file=sys.stderr)
    rc = subprocess.run(cmd, shell=True).returncode
    report.append('[run:%4d] (%10.2f) %s' % (rc, now()-st, cmd))
    print(report[-1], file=sys.stderr)
    return rc


# vmtouch
run('git clone https://github.com/hoytech/vmtouch.git /tmp/build_vmtouch')
run('cd /tmp/build_vmtouch && make && sudo make install')

# CPU instance tools
run('pip install gdown tqdm')
run('pip install seaborn sklearn numpy pandas scipy')
run('pip install ipdb loguru psutil sympy')


# update /usr/local/bin
# (for root) You can do the same thing in /usr/local/sbin if needed
run('eval "$(pyenv init -)"')
run('pyenv rehash')
run('sudo ln -s ~/.pyenv/shims/* /usr/local/bin/')

print('================================', file=sys.stderr)
print('==============DONE==============', file=sys.stderr)
print('================================', file=sys.stderr)
sys.stderr.flush()

json.dump(report, sys.stdout, indent=1)
sys.stdout.flush()
