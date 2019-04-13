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
run('pyenv install miniconda3-4.3.30')
run('pyenv virtualenv miniconda3-4.3.30 mini368')
run('pyenv global mini368')
run('eval "$(pyenv init -)"')
run('eval "$(pyenv virtualenv-init -)"')


r"""
➜  .pyenv git:(master) pyenv install miniconda3-4.3.30
➜  .pyenv git:(master) pyenv virtualenv miniconda3-4.3.30 mini368
➜  .pyenv git:(master) pyenv global mini368

"""