#!/bin/bash

# OFS: output separator
# NR: number of record

# awk 'BEGIN{cmds} pattern{cmds} END{cmds}'

awk '$3 ~ /root/ || NR == 1 {print NR, $0}' file.txt    # ~ means: regular expression

awk '$3=="testuser" && $5==85{print $0}' file.txt

awk 'BEGIN{FS="Jun"} {print $1, " * ", $2}' file.txt

awk 'NR==5{print;exit}' f1
