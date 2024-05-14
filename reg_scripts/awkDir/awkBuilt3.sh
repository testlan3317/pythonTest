#!/bin/bash
# -F: separator
# awk 'BEGIN {FS=":"} {print $1, $4;}' /etc/passwd
# note the comma(,) needs to be added between variables. 
#
awk -F ':' '{print $1,$4;}' /etc/passwd
