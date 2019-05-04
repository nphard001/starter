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

run('git clone https://github.com/hoytech/vmtouch.git /tmp/build_vmtouch')
run('cd /tmp/build_vmtouch && make && sudo make install')

run('pip install mako')
run('pip install django')
run('pip install django-sslserver')
run('CC=/usr/bin/clang pip install uwsgi')
# (macbook) more specfially the openssl path
# run('CFLAGS="-I/usr/local/opt/openssl/include" LDFLAGS="-L/usr/local/opt/openssl/lib" CC=/usr/bin/clang pip install uwsgi')

run('pip install sympy')
run('pip install pandas')
run('pip install lightgbm')
run('pip install tensorflow tensorflow-gpu')
run('pip install torch torchvision')

# ADL-HW2 uses
run('pip install cython')
run('pip install fastText')
run('pip install tqdm')
run('pip install python-box')
run('pip install pyyaml')
run('pip install ipdb')
run('pip install SpaCy')
run('pip install NLTK')


# update /usr/local/bin
# (for root) You can do the same thing in /usr/local/sbin if needed
run('eval "$(pyenv init -)"')
run('pyenv rehash')
run('sudo ln -s ~/.pyenv/shims/* /usr/local/bin/')
# sudo ln -s /home/cnlab/.pyenv/versions/miniconda3-4.3.30/bin/* /usr/local/bin/

# new bin setups

print('================================', file=sys.stderr)
print('==============DONE==============', file=sys.stderr)
print('================================', file=sys.stderr)
sys.stderr.flush()

json.dump(report, sys.stdout, indent=1)
sys.stdout.flush()