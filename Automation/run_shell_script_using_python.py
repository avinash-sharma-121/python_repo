import subprocess

#simple run
subprocess.run(["sh","./script.sh"])

#store the output
result=subprocess.run(["sh","./script.sh"], capture_output=True)
