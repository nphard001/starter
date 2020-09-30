import os, sys, json
import datetime
import subprocess
now = lambda: datetime.datetime.now().timestamp()
report = []
def run(cmd):
    global report
    st = now()
    print('[run]', cmd, file=sys.stderr)
    rc = subprocess.run(cmd, shell=True).returncode
    report.append('[run:%4d] (%10.2f) %s'%(rc, now()-st, cmd))
    print(report[-1], file=sys.stderr)
    return rc

run('git clone https://github.com/pyenv/pyenv.git ~/.pyenv')
run('sudo ln -s ~/.pyenv/bin/pyenv /usr/local/bin/pyenv')
run('sudo ln -s ~/.pyenv/bin/pyenv /usr/local/sbin/pyenv')
run('eval "$(pyenv init -)"')
run('pyenv install miniconda3-4.3.30')
run('pyenv global miniconda3-4.3.30')
run('pyenv rehash')
run('pyenv exec conda update conda -y')
run('sudo ln -fvs ~/.pyenv/shims/* /usr/local/bin/')

run('sudo mkdir /active')
run('sudo mkdir /tmp2')
run('sudo mkdir /dat')
run('echo "/active" > ~/.pyenv/versions/miniconda3-4.3.30/lib/python3.6/site-packages/qtwu.pth')
run('echo "all : ; echo start" > /active/startup.makefile')

print('================================', file=sys.stderr)
print('==============DONE==============', file=sys.stderr)
print('================================', file=sys.stderr)
sys.stderr.flush()

json.dump(report, sys.stdout, indent=1)
sys.stdout.flush()