import subprocess
p = subprocess.run("uname -a", shell=True, stdout=subprocess.PIPE)
print(p.stdout.decode('utf-8'))
