import subprocess
import os

print(os.getcwd())

#simple run
#subprocess.run(["sh","../scripts/demo.sh"])

#store the output
result=subprocess.run(["sh","../scripts/demo.sh"], capture_output=True,text=True)

#print("Return Code:", result.returncode)
print("Output:", result.stdout)
print("Error:", result.stderr)

