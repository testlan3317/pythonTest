#!/bin/bash
# -f: program file
#
awk -F: -f testfile /etc/passwd
