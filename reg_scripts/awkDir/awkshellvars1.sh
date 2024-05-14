#!/bin/bash

username="testuser"

# ~ is for matching regular expression
cat /etc/passwd | awk -v name="$username" ' $0 ~ name {print $0}'  
