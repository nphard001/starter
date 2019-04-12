import sys
import subprocess
def run(cmd):
    print('[run]', cmd, file=sys.stderr)
    return subprocess.run(cmd, shell=True).returncode

run('git clone https://github.com/pyenv/pyenv.git ~/.pyenv')
run('sudo ln -s ~/.pyenv/bin/pyenv /usr/local/bin/pyenv')
run('sudo ln -s ~/.pyenv/bin/pyenv /usr/local/sbin/pyenv')
run('git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv')
run('eval "$(pyenv init -)"')
run('eval "$(pyenv virtualenv-init -)"')
