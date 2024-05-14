#!/bin/bash

awk 'END {print "number of records in file is: ", NR}' ./domains.txt

