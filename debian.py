import sys
import datetime
import subprocess
now = lambda: datetime.datetime.now().timestamp()
run = lambda cmd: subprocess.run(cmd, shell=True)
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
    "libreadline-dev",               # for SoftEth
    "libssl-dev",                    # for SoftEth, aka openssl-devel
    "libncurses5-dev",               # for SoftEth
    "libncursesw5-dev",              # for SoftEth
    "libz-dev",                      # for SoftEth (-lz)
    # "linux-headers-4.9.0-8-amd64",   # (kernel-tree) for gcp nvidia driver
]
cmd_list = [
    "sudo apt-get update",
]
cmd_list.extend([
    "sudo apt-get install -y %s"%pkg
    for pkg in pkg_list
])
print(cmd_list)
