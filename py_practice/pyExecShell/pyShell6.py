# More advanced example - how to access a server with ssh and the subprocess module:

import subprocess

ssh = subprocess.Popen(["ssh", "-i .ssh/id_rsa", "user@host"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                bufsize=0)

# send ssh commands to stdin
ssh.stdin.write("uname -a\n")
ssh.stdin.write("uptime\n")
ssh.stdin.close()

# Fetch output
for line in ssh.stdout:
    print(line.strip())

# set bufsize=0, in order to have unbuffered output.
# after finished wrting, you need to close the "stdin"
