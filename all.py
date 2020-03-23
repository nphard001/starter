r'''
sudo apt-get install -y tmux
tmux new -s install
'''
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
# ================================================================
run('python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/debian.py --no-cache --quiet -O -)" > debian_stdout.json')
run('python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/ohmyzsh.py --no-cache --quiet -O -)" > ohmyzsh_stdout.json')
run('python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/pyenv.py --no-cache --quiet -O -)" > pyenv_stdout.json')
run('python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/pkg368.py --no-cache --quiet -O -)" > pkg368_stdout.json')
run('python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/pkg368_jupyter.py --no-cache --quiet -O -)" > pkg368_jupyter_stdout.json')
run('python3 -c "$(wget https://raw.githubusercontent.com/nphard001/starter/master/jcustom.py --no-cache --quiet -O -)" > jcustom_stdout.json')
# ================================================================

print('================================', file=sys.stderr)
print('==============DONE==============', file=sys.stderr)
print('================================', file=sys.stderr)
sys.stderr.flush()

json.dump(report, sys.stdout, indent=1)
sys.stdout.flush()