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

path_key = '~/.ssh/pkg368key.key'
path_pem = '~/.ssh/pkg368cert.pem'
run(r'openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout {path_key} -out {path_pem} -subj /C=XD'.format(**locals()))
run('pip install jupyter')
run('pip install jupyter_contrib_nbextensions')
run('pip install jsonschema') # for jupyter extensions

run('eval "$(pyenv init -)"')
run('pyenv rehash')
run('sudo ln -s ~/.pyenv/shims/* /usr/local/bin/')

run('jupyter contrib nbextension install --user')
run('jupyter nbextensions_configurator enable --user')


print('================================', file=sys.stderr)
print('==============DONE==============', file=sys.stderr)
print('================================', file=sys.stderr)
sys.stderr.flush()

json.dump(report, sys.stdout, indent=1)
sys.stdout.flush()