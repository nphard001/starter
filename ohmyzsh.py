import sys
import subprocess
def run(cmd):
    print('[run]', cmd, file=sys.stderr)
    return subprocess.run(cmd, shell=True).returncode

run('sudo apt-get install -y zsh')
run('sh -c "$(wget https://raw.githubusercontent.com/nphard001/oh-my-zsh/master/tools/install.sh -O -)"')
