import sys
import subprocess
def run(cmd):
    print('[run]', cmd, file=sys.stderr)
    return subprocess.run(cmd, shell=True).returncode

run('git clone https://github.com/pyenv/pyenv.git ~/.pyenv')
run('sudo ln -s ~/.pyenv/bin/pyenv /usr/local/bin/pyenv')
run('sudo ln -s ~/.pyenv/bin/pyenv /usr/local/sbin/pyenv')
run('eval "$(pyenv init -)"')
run('pyenv install miniconda3-4.3.30')
run('pyenv global miniconda3-4.3.30')
run('pyenv rehash')
run('pyenv exec conda update conda -y')
run('sudo ln -s ~/.pyenv/shims/* /usr/local/bin/')

