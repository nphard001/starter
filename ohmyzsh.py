import sys
import subprocess
def run(cmd):
    print('[run]', cmd, file=sys.stderr)
    return subprocess.run(cmd, shell=True).returncode

run(f'sudo apt-get install -y zsh')
run(f'sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"')
