#!/bin/bash
# -F: separator
# awk 'BEGIN {FS=":"} {print $1, $4;}' /etc/passwd
# note the comma(,) needs to be added between variables. 
#
# OFS: output separator
awk -F ':' 'BEGIN{OFS="==>"} {print $1,$4;}' /etc/passwd
