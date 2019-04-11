import sys
import datetime
import subprocess
now = lambda: datetime.datetime.now().timestamp()
def run(cmd):
    proc = subprocess.Popen(cmd, 
      shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    rst = proc.communicate()
    proc.wait()
    return {
        "stdout": rst[0].decode("utf-8").strip(),
        "stderr": rst[1].decode("utf-8").strip(),
        "rc": proc.returncode,
    }

pkg_list = [
    "rsync",                         
    "tmux",                          
    "htop",                          
    "make",                          
    "vim",                           
    "git",                           
    "g++",                           # may fail?
    "gdb",                           # may fail?
    "cmake",                         # may fail?
    "bzip2",                         # unzip python things
    "unzip",                         # unzip python things
    "strace",                        # systemcall trace
    "traceroute",                    # network test internal IP
    "nload",                         # network usage
    "zlib1g-dev",                    # ubuntu python365
    "libssl-dev",                    # for SoftEth, aka openssl-devel
    "libz-dev",                      # for SoftEth (-lz)
    "libreadline-dev",               # for SoftEth
    "libncurses5-dev",               # for SoftEth
    "libncursesw5-dev",              # for SoftEth
    # "linux-headers-4.9.0-8-amd64",   # (kernel-tree) for gcp nvidia driver
]
cmd_list = [
    "sudo apt-get update",
]
# cmd_list.extend([
#     "sudo apt-get install -y %s"%pkg
#     for pkg in pkg_list
# ])
cmd_list.append("sudo apt-get install -y %s"%(" ".join(pkg_list)))
rc_total = 0
for cmd in cmd_list:
    st = now()
    sys.stderr.write('\rrun: %48s'%(cmd))
    sys.stderr.flush()
    rst = run(cmd)
    rc_total = rc_total or rst['rc']
    sys.stderr.write(' %9.4f return %d\n'%(now()-st, rst['rc']))
    sys.stderr.flush()
    for fd in ['stdout', 'stderr']:
        if len(rst[fd])>0:
            print("# "+fd)
            print(rst[fd])

sys.exit(rc_total)

