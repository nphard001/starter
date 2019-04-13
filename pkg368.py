import sys
import subprocess
def run(cmd):
    print('[run]', cmd, file=sys.stderr)
    return subprocess.run(cmd, shell=True).returncode

run('git clone https://github.com/hoytech/vmtouch.git /tmp/build_vmtouch')
run('cd /tmp/build_vmtouch && make && sudo make install')



run('eval "$(pyenv init -)"')
run('pyenv rehash')
run('sudo ln -s ~/.pyenv/shims/* /usr/local/bin/')

