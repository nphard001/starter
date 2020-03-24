import subprocess
p = subprocess.run("uname -a", shell=True, timeout=timeout, stdout=subprocess.PIPE)
print(p.stdout)
