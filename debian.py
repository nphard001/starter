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

pkg_list = [
    "rsync",                         
    "tmux",                          
    "htop",                          
    "make",                          
    "vim",                           
    "git",                           
    "tree",                          # take a glimpse in directories
    "g++",                           # may fail?
    "gdb",                           # may fail?
    "cmake",                         # may fail?
    "clang",                         # use it when gcc fail, like `pip install uwsgi`
    "xauth",                         # X11 display
    "bzip2",                         # unzip python things
    "unzip",                         # unzip python things
    "strace",                        # systemcall trace
    "traceroute",                    # network test internal IP
    "lsof",                          # debug open files
    "nload",                         # network usage
    "zlib1g-dev",                    # ubuntu python365
    "libssl-dev",                    # for SoftEth, aka openssl-devel
    "libz-dev",                      # for SoftEth (-lz)
    "libreadline-dev",               # for SoftEth
    "libncurses5-dev",               # for SoftEth
    "libncursesw5-dev",              # for SoftEth
    # "linux-headers-4.9.0-8-amd64",   # (kernel-tree) for gcp nvidia driver
    # "libav-tools",                   # adl3 # too many dependencies
]
cmd_list = [
    "apt install sudo", # first you have to "su", um...
    "sudo apt-get update",
]
cmd_list.extend([
    "sudo apt-get install -y %s"%pkg
    for pkg in pkg_list
])

# in one command
# cmd_list.append("sudo apt-get install -y %s"%(" ".join(pkg_list)))

rc_total = 0
for cmd in cmd_list:
    run(cmd)

print('================================', file=sys.stderr)
print('==============DONE==============', file=sys.stderr)
print('================================', file=sys.stderr)
sys.stderr.flush()

json.dump(report, sys.stdout, indent=1)
sys.stdout.flush()