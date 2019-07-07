import os
import sys
import hashlib
import tempfile
import datetime
import subprocess
md5 = lambda x: hashlib.md5(x.encode('utf-8')).hexdigest()
now = lambda: datetime.datetime.now().timestamp()
def run(cmd):
    print('[run]', cmd, file=sys.stderr)
    return subprocess.run(cmd, shell=True).returncode
user_at_host = sys.argv[1]
symbol = 'key_'+md5(user_at_host)[:7]
key_dir = '~/.ssh'
key_private = os.path.join(key_dir, symbol)
key_public = os.path.join(key_dir, symbol+'.pub')

# remote authorized_keys
run(f'ssh-keygen -f {key_private} -t ecdsa -b 521')
run(f'scp {key_public} {user_at_host}:~/.ssh_key_tmp')
run(f'ssh {user_at_host} "mkdir ~/.ssh ; cat ~/.ssh_key_tmp >> ~/.ssh/authorized_keys"')

# local config file
lst2 = user_at_host.split('@')
host = lst2[-1]
if len(lst2)==2:
    user = lst2[0]
else:
    user = os.getenv('USER')

config = '~/.ssh/config'
config_to_add = tempfile.NamedTemporaryFile(mode="w")
config_to_add.file.write('\n'+f'''
Host {host}
  HostName {host}
  User {user}
  IdentityFile {key_private}
  IdentitiesOnly yes
    '''.strip()+'\n')
config_to_add.file.flush()
run(f'cat {config_to_add.name} >> {config}')
