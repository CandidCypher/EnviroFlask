import subprocess
thread = subprocess.Popen('rsync -recursive -e "ssh" /home/cameron/Documents/Workspace/EnviroFlask/ pi@monitor.local:/home/pi/EnviroFlask')
thread.communicate("raspberry")