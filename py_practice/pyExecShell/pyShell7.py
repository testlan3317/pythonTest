import subprocess

commands = ["echo 'another command'", "cd /home/zhengj/", "ls -l", "lsblk"]
p = subprocess.Popen(['ssh', 'user@host',';'.join(commands)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = p.communicate()
listoutput = str(stdout).split("\\n")

print(type(listoutput))
list_len = len(listoutput)
print(f"the len of list is {list_len}")
print(listoutput)
print(listoutput[0])
print(listoutput[1])
print(listoutput[2])
print(listoutput[3])
print(listoutput[4])
print(listoutput[5])
print(listoutput[6])
print(listoutput[7])
print(listoutput[8])

