import sys
import datetime
import subprocess
now = lambda: datetime.datetime.now().timestamp()
report = []
def run(cmd):
    global report
    st = now()
    print('[run]', cmd, file=sys.stderr)
    rc = subprocess.run(cmd, shell=True).returncode
    report.append('[run: %2d] (%10.2f) %48s'%(rc, now()-st, cmd))
    return rc

run('git clone https://github.com/hoytech/vmtouch.git /tmp/build_vmtouch')
run('cd /tmp/build_vmtouch && make && sudo make install')

path_key = '~/.ssh/pkg368key.key'
path_pem = '~/.ssh/pkg368cert.pem'
run(r'openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout {path_key} -out {path_pem} -subj /C=XD'.format(**locals()))
run('pip install jupyter')

run('pip install mako')
run('pip install django')
run('pip install django-sslserver')



run('eval "$(pyenv init -)"')
run('pyenv rehash')
run('sudo ln -s ~/.pyenv/shims/* /usr/local/bin/')

print('================================')
print('\n'.join(report))
