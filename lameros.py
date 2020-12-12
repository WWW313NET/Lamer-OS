import subprocess
def _init_():
    cli = input("kali@lincox~# ")
    subprocess.call(cli, shell=True)
while True:
    _init_()
