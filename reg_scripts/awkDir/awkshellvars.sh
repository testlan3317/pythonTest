#!/bin/bash

read -p "Please enter username: " username
echo $username
# search for username in /etc/passwd
# "/$username/" is the regular expression
#
#
 cat /etc/passwd | awk "/$username/"'{ print $0 }'
