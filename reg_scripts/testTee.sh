#!/bin/bash

# hide the output :    df -h | tee diskusage.txt > /dev/null
df -h | tee diskusage.txt


#sudo echo "hello"> /etc/file.conf will fail because the redirection of outpu is not performed by sudo
# use below instead:
#
# echo "hello"|sudo tee -a /etc/file.conf >/dev/null
#
